from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_listings, name='job_listings'),
    path('create/', views.create_offer, name='create_offer'),
    path('job-details/<int:pk>', views.job_details, name='job_details'),
]
