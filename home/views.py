from django.shortcuts import render
import datetime
from jobs.models import Job
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 15)  # Cache for 15 minutes
def home(request):
    year = datetime.date.today().year
    jobs = Job.objects.all()[:3]
    return render(request, 'home/main.html',context={'year': year, 'jobs': jobs})
