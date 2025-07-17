from django.shortcuts import render
from testimonials.models import Tmonials
# Create your views here.
def services(request):
    tests = Tmonials.objects.all()[:6]
    return render(request, 'services/services.html', {'tests': tests})