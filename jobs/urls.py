from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_listings, name='job_listings'),
    path('create/', views.create_offer, name='create_offer')
]
