from django.shortcuts import render, redirect
from .forms import CreateJobForm, CandidateApplicationForm
from django.contrib import messages
from .models import Job, CandidateDetails
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from django.db.models import Q

# Create your views here.
def job_listings(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_listings.html', context={'jobs':jobs   })


def create_offer(request):
    user = request.user
    # Safe check for permissions
    is_head_recruiter = False
    if hasattr(user, 'recruiter_profile'):
        is_head_recruiter = user.recruiter_profile.is_head_recruiter

    if not (user.is_admin or user.is_superuser or is_head_recruiter):
        return HttpResponseForbidden("You don't have permission to access this page")
    
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user  # Set the user manually
            job.save()
            messages.success(request, 'Job offer added successfully!')
            return redirect('admin_dashboard')  # replace with your success redirect
        else:
            messages.error(request, 'Details entered are not valid, check errors below.')
    else:
        form = CreateJobForm()
    return render(request, 'jobs/create_job.html', context={'form': form})

def job_details(request, pk):
    job = get_object_or_404(Job, id=pk)
    return render(request, 'jobs/job_details.html', context={'job':job})


def candidate_application(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = CandidateApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job  # Link to the job
            application.save()
            # Store in session that they completed the form
            request.session['application_submitted'] = True

            return redirect('success_application', job_id=job.id)
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = CandidateApplicationForm()
    return render(request, 'jobs/candidate/candidate_form.html', context={'job':job, 'form':form})

def application_success(request, job_id):
    # Only allow access if they submitted the form
    if not request.session.get('application_submitted'):
        return redirect('job_listings')
    
    # Clear the session flag
    request.session.pop('application_submitted', None)
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/candidate/success_application.html', {'job': job})


def view_applications(request):
    applications = CandidateDetails.objects.all().select_related('job')
    all_jobs = Job.objects.all()
    # Filtering
    search_query = request.GET.get('search')
    job_filter = request.GET.get('job')
    status_filter = request.GET.get('status')
    
    if search_query:
        applications = applications.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(whatsapp__icontains=search_query)
        )
    if job_filter:
        applications = applications.filter(job_id=job_filter)
    
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    context = {
        'applications': applications,
        'all_jobs': all_jobs,
    }
    
    return render(request, 'jobs/candidate/candidate_apps.html', context)

def application_status_changer(request, pk):
    application = get_object_or_404(CandidateDetails, id=pk)
    return render('jobs/candidate/candidate_apps.html', context={})

