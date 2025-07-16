from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tmonials
# Create your views here.
@login_required
def tmonials(request):
    tmonials = Tmonials.objects.all()
    if request.method == 'POST':
        pass
    else: 
        pass
    return render(request, 'tmonials/tmonials.html', context={'testimonials': tmonials})
