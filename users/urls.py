from django.urls import path
from . import views
urlpatterns = [
    path('admin-dash', views.admin_dash, name='admin_dash')
]