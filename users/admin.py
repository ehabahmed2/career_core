from django.contrib import admin
from .models import AdminProfile, BaseUser, RecruiterProfile  # Add RecruiterProfile import
from jobs.models import Job
from testimonials.models import Tmonials


# Admin Profile Inline
class AdminProfileInline(admin.StackedInline):
    model = AdminProfile

# Recruiter Profile Inline
class RecruiterProfileInline(admin.StackedInline):
    model = RecruiterProfile
    fields = ('is_approved', 'is_head_recruiter')  # Explicitly show these fields

@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    inlines = [RecruiterProfileInline, AdminProfileInline]

admin.site.register(Job)
admin.site.register(Tmonials)