from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import random
# base user to inhirit from
class BaseUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        RECRUITER = 'recruiter', 'Recruiter'  
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.RECRUITER  # Added default
    )

    full_name = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=20)  
    address = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(
        upload_to='profiles/%y/%m/%d',
        default='profiles/default.svg',
        blank=True,
        null=True,
    )
    
    username = models.CharField(
        max_length=255,
        unique=True,
        help_text='Optional, 255 charachters or fewer'
    )
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username',]  
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    @property
    def is_recruiter(self):
        return self.role == self.Role.RECRUITER

    class Meta:
        verbose_name = 'Base User'
        verbose_name_plural = 'Base Users'
    
    def __str__(self):
        return self.full_name

class AdminProfile(models.Model):  
    user = models.OneToOneField(
        BaseUser,
        on_delete=models.CASCADE,
        related_name='admin_profile' 
    )
    is_approver = models.BooleanField(default=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Admin Profile'
        verbose_name_plural = 'Admin Profiles'
    
    def __str__(self):
        return f"{self.user.full_name} (Admin)"  # Fixed: access via user

class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        BaseUser,
        on_delete=models.CASCADE,
        related_name='recruiter_profile'
    )
    is_approved = models.BooleanField(default=False)
    is_head_recruiter = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Recruiter Profile'
        verbose_name_plural = 'Recruiter Profiles'
    
    def __str__(self):
        return f"{self.user.full_name} (Recruiter)"


# models.py

User = get_user_model()

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    @classmethod
    def generate_token(cls):
        return str(random.randint(100000, 999999))  # 6-digit token
