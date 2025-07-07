from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_listings, name='job_listings')
]
