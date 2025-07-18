from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    
    # testimonials
    path('testimonials/<int:pk>/action/', views.tmonial_action, name='tmonial_action'),
    
    # rset the password
    path('password-reset/', views.send_reset_token, name='password_reset'),
    path('token-verification/', views.verify_token, name='token_verification'),
    path('new-password/', views.new_password, name='new_password'),
    path('password-reset-success/', views.password_reset_complete, name='password_reset_complete'),
]

