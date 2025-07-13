from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    year = datetime.date.today().year
    return render(request, 'home/main.html',context={'year': year})
