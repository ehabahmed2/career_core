from django.shortcuts import render
import datetime
from jobs.models import Job

# Create your views here.

def home(request):
    year = datetime.date.today().year
    jobs = Job.objects.all()[:3]
    return render(request, 'home/main.html',context={'year': year, 'jobs': jobs})
