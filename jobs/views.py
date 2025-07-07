from django.shortcuts import render

# Create your views here.
def job_listings(request):
    return render(request, 'jobs/job_listings.html', context={})