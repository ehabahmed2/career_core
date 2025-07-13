from django.db import models
from django.utils import timezone

# Create your models here.
class Tmonials(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profiles/testimonials/%y/%m/%d', blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = 'Testimonial'
    
    def __str__(self):
        return self.name
