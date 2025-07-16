from django.shortcuts import render
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
load_dotenv()

# Create your views here.
def contact(request):
    send_mail(
    'title of message',
    f"Message from Name -- Email -- contenct \n Message",
    os.getenv('EMAIL_HOST_PASSWORD'),  
    os.getenv('EMAIL_HOST_PASSWORD'),  
    fail_silently=False,
)
    return render(request, 'contact/contact.html', context={})