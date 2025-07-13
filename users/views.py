from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BaseUser
from jobs.models import Job
from django.http import HttpResponseForbidden
from testimonials.models import Tmonials
# Create your views here.

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
    return render(request, 'users/admin_dash.html', context=context)