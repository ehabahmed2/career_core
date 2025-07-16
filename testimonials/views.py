from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tmonials
from .forms import TmonialsForm
from django.contrib import messages


def tmonials(request):
    tmonials = Tmonials.objects.all()
    if request.method == 'POST':
        form = TmonialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for the testimonial!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong details entered!')
    else: 
        form = TmonialsForm()
    return render(request, 'tmonials/tmonials.html', context={'testimonials': tmonials, 'form':form})


