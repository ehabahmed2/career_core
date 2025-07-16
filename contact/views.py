from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm  # You'll need to create this form

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    subject=f"New Contact Form Submission: {form.cleaned_data['subject']}",
                    message=f"""
                    Name: {form.cleaned_data['name']}
                    Email: {form.cleaned_data['email']}
                    Message: {form.cleaned_data['message']}
                    """,
                    from_email=settings.EMAIL_HOST_USER ,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})