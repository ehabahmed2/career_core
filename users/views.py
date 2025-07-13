from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import BaseUser
from jobs.models import Job
from django.http import HttpResponseForbidden
from testimonials.models import Tmonials
from .forms import LoginForm, RegisterForm
import secrets
from django.core.cache import cache 

# Create your views here.
User = get_user_model()

# get current user
@login_required
def admin_dash(request):
    if not (request.user.is_admin or request.user.is_superuser):
        return HttpResponseForbidden("You don't have permission to access this page")
    # Get recruiters with their users and related data
    recruiters = BaseUser.objects.filter(role=BaseUser.Role.RECRUITER).select_related('recruiter_profile')
    # get available offers
    jobs = Job.objects.all()
    
    # get testimonials
    testimonials = Tmonials.objects.all()
    
    context = {
        'recruiters': recruiters,
        'jobs': jobs,
        'testimonials': testimonials,
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
    return render(request, 'users/admins/login.html', context={'form': form})


# register user
def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are logged in already!')
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            # if form is valid then save it to db
            if form.is_valid():
                user = form.save()
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
    return render(request, 'users/admins/register.html', context={'form':form})


def registration_success(request, token):
    if not cache.get(f'reg_success_{token}'):
        messages.warning(request, "Invalid or expired registration token")
        return redirect('register')
    
    # Delete token after use
    cache.delete(f'reg_success_{token}')
    return render(request, 'users/registration_success.html', context={})

