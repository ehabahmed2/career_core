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
    price = models.PositiveBigIntegerField(default=0)
    company = models.CharField(max_length=255, default='N/A')
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['created_at']
    def __str__(self):
        return self.title


