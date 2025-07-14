from django.shortcuts import render, redirect
from .forms import CreateJobForm
from django.contrib import messages
from .models import Job
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

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