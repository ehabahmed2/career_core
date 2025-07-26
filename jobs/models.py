from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    price = models.PositiveBigIntegerField()
    company = models.CharField(max_length=255)
    job_type = models.CharField(max_length=155, default='Full-time')
    experience = models.CharField(max_length=155, default='N/A')
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['created_at']
    def __str__(self):
        return self.title


class CandidateDetails(models.Model):
    EDUCATION_CHOICES = [
        ('undergraduate', 'Undergraduate Student'),
        ('graduate', 'Graduate'),
    ]
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    full_name = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    # Additional Languages (optional)
    other_language_1 = models.CharField(max_length=50, blank=True, null=True)
    other_language_2 = models.CharField(max_length=50, blank=True, null=True)
    
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='pending', max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.job.title if self.job else 'No Job'}"
    class Meta:
        verbose_name = 'Candidate Application'
        verbose_name_plural = 'Candidate Applications'
        ordering = ['-application_date']


