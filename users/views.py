from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import BaseUser, RecruiterProfile, AdminProfile
from jobs.models import Job
from django.http import HttpResponseForbidden, JsonResponse
from testimonials.models import Tmonials
from .forms import LoginForm, RegisterForm, UserUpdateForm
import secrets
from django.core.cache import cache 
from django.views.decorators.http import require_POST

from jobs.models import CandidateDetails
from jobs.forms import CreateJobForm


# Create your views here.
User = get_user_model()

# get current user
@login_required
def admin_dash(request):
    user = request.user
    # Safe check for permissions
    is_head_recruiter = False
    if hasattr(user, 'recruiter_profile'):
        is_head_recruiter = user.recruiter_profile.is_head_recruiter

    if not (user.is_admin or user.is_superuser or is_head_recruiter):
        return HttpResponseForbidden("You don't have permission to access this page")
    
    # Get recruiters with their users and related data
    recruiters = BaseUser.objects.filter(role=BaseUser.Role.RECRUITER).select_related('recruiter_profile')
    # get available offers
    jobs = Job.objects.all()
    
    # get testimonials
    testimonials = Tmonials.objects.all()
    
    applications = CandidateDetails.objects.all()[:6]
    
    context = {
        'recruiters': recruiters,
        'jobs': jobs,
        'testimonials': testimonials,
        'applications': applications,
        
    }
    return render(request, 'users/admins/admin_dash.html', context=context)

# log in form
def login_form(request):
    # check that the user isn'
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already!')
        return redirect('home')
    else:
        if request.method == 'POST': 
            form = LoginForm(request.POST)
            if form.is_valid():
                #authenticate user
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=email, password=password)
                # log in the user if it does exist
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome to Career Core')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid log in details')
        else: 
            form = LoginForm()
    return render(request, 'users/login.html', context={'form': form})

@login_required
def logout_form(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')

# register user
def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already!')
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST, request.FILES)
            # if form is valid then save it to db
            if form.is_valid():
                user = form.save()
                RecruiterProfile.objects.create(user=user)
                messages.success(request, 'Registered successfully!')
                # Generate unique token
                token = secrets.token_urlsafe(32)
                # Store token in cache with 5 minute expiration
                cache.set(f'reg_success_{token}', True, 300)
                
                return redirect('registration_success', token=token)
            else: 
                messages.warning(request, 'Error with the details provided, kindly check your inputs!')
        else:
            form = RegisterForm()
    return render(request, 'users/register.html', context={'form':form})


def registration_success(request, token):
    if not cache.get(f'reg_success_{token}'):
        messages.warning(request, "Invalid or expired registration token")
        return redirect('register')
    
    # Delete token after use
    cache.delete(f'reg_success_{token}')
    return render(request, 'users/registration_success.html', context={})


@login_required
def all_recruiters(request):
    user = request.user

    # Safe check for permissions
    is_head_recruiter = False
    if hasattr(user, 'recruiter_profile'):
        is_head_recruiter = user.recruiter_profile.is_head_recruiter

    if not (user.is_admin or user.is_superuser or is_head_recruiter):
        return HttpResponseForbidden("You don't have permission to access this page")
    
    else:
        recruiters = BaseUser.objects.filter(role=BaseUser.Role.RECRUITER).select_related('recruiter_profile')

    return render(request, 'users/all_recruiters.html', context={'recruiters': recruiters})


@require_POST
def recruiter_action(request, recruiter_id):
    user = request.user
    recruiter = get_object_or_404(BaseUser, id=recruiter_id)

    # make sure the target actually has a profile
    try:
        profile = recruiter.recruiter_profile
    except RecruiterProfile.DoesNotExist:
        messages.error(request, "Recruiter profile not found")
        return redirect('all_recruiters')

    # Prevent heads from touching other heads (unless you're admin/superuser)
    if profile.is_head_recruiter and not (user.is_admin or user.is_superuser):
        messages.error(request, "You cannot perform that action on another Head Recruiter.")
        return redirect('all_recruiters')
    
    action = request.POST.get('action')

    profile = recruiter.recruiter_profile

    if action == 'approve':
        profile.is_approved = True
        profile.save()
        messages.success(request, f"Approved {recruiter.full_name}")
    elif action == 'promote' and profile.is_head_recruiter:
        profile.is_head_recruiter = True
        profile.save()
        messages.success(request, f"Promoted {recruiter.full_name} to Head Recruiter")
    elif action == 'suspend':
        profile.is_approved = False
        profile.save()
        messages.success(request, f"Suspended {recruiter.full_name}")
    elif action == 'unsuspend':
        profile.is_approved = True
        profile.save()
        messages.success(request, f"Unsuspended {recruiter.full_name}")
    elif action == 'delete':
        recruiter.delete()
        messages.success(request, f"Deleted {recruiter.full_name}")
    else:
        messages.error(request, "Invalid action or You don't have permision to do so")


    return redirect('all_recruiters')

# user's profile
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

#update user's profile
@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if request.user.is_admin:
            form = AdminProfile(request.POST, instance=user.admin_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Something wrong with the details entered!')
        
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'users/profile_update.html', context={'form':form})

@login_required
def edit_job(request, pk):
    user = request.user
    # Safe check for permissions
    is_head_recruiter = False
    if hasattr(user, 'recruiter_profile'):
        is_head_recruiter = user.recruiter_profile.is_head_recruiter

    if not (user.is_admin or user.is_superuser or is_head_recruiter):
        return HttpResponseForbidden("You don't have permission to access this page")
    
    job = get_object_or_404(Job, id=pk)
    if request.method == 'POST':
        form = CreateJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated offer')
            return redirect('admin_dashboard')
    else:
        form = CreateJobForm(instance=job)
    return render(request, 'jobs/edit_job.html', context={'form':form})


@require_POST
def job_action(request, pk):
    user = request.user
    # Safe check for permissions
    is_head_recruiter = False
    if hasattr(user, 'recruiter_profile'):
        is_head_recruiter = user.recruiter_profile.is_head_recruiter

    job = get_object_or_404(Job, id=pk)
    
    # validate status
    valid_status = ['suspend', 'activate', 'delete']
    new_status = request.POST.get('status')
    
    if new_status in valid_status:
        if new_status == 'suspend':
            job.is_active = False
            job.save()
        elif new_status == 'activate':
            job.is_active = True
            job.save()
        else:
            job.delete()
        messages.success(request, f"Action to {new_status} is Done. :)")
        return redirect('admin_dashboard')
    else:
        messages.error(request, 'Not valid status!')

    return render(request, 'users/admins/admin_dash.html', context={})

def tmonial_action(request, pk):
    if request.method == 'POST':
        testimonial = get_object_or_404(Tmonials, id=pk)
        if request.POST.get('delete_test'):
            testimonial.delete()
            messages.success(request, 'Testimonial is deleted!')
            return redirect('admin_dashboard')
    return render(request, 'users/admins/admin_dash.html', {})
