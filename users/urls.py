from django.urls import path
from . import views
urlpatterns = [
    path('admin-dash/', views.admin_dash, name='admin_dashboard'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('register/', views.register, name='register'),
    
    path('registration-success/<str:token>/', views.registration_success, name='registration_success'),
    path('all-recruiters/', views.all_recruiters, name='all_recruiters'),
    path('recruiters/<int:recruiter_id>/action/', views.recruiter_action, name='recruiter_action'),
    
    # update user profile
    path('profile/update/', views.update_profile, name='profile_update'),
    path('profile/', views.profile, name='profile'),
    
    # job offers
    path('job/<int:pk>', views.edit_job, name='edit_job'),
    path('jobs/<int:pk>/action/', views.job_action, name='job_action'),
]

