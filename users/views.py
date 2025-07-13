from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import BaseUser
from jobs.models import Job
from django.http import HttpResponseForbidden
from testimonials.models import Tmonials
from .forms import LoginForm

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
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, 'Invalid log in details')
        else: 
            form = LoginForm()
    return render(request, 'users/admins/login.html', context={'form': form})