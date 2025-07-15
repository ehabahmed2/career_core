from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_listings, name='job_listings'),
    path('create/', views.create_offer, name='create_offer'),
    path('job-details/<int:pk>/', views.job_details, name='job_details'),
    path('application/<int:job_id>', views.candidate_application, name='candidate_application'),
    path('success-application/<int:job_id>', views.application_success, name='success_application'),
    
    path('all-applications/', views.view_applications, name='all_applications'),
    path('all-applications/<int:pk>/', views.application_status_changer, name='update_candidate_statu'),
]
