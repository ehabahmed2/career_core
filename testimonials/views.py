from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def tmonials(request):
    return render(request, 'tmonials/tmonials.html', context={})