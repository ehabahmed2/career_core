from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.sitemaps import views as sitemap_views


class QuickSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'about',
            'contact',
            'job_listings',
            'services',
            'tmonials'
        ]
    
    def location(self, item):
        return reverse(item)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('jobs/', include('jobs.urls')),
    path('contact/', include('contact.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('users/', include('users.urls')),
    path('services/', include('services.urls')),
    
    # using the imported sitemap view function
    path('sitemap.xml/', sitemap_views.sitemap, 
         {'sitemaps': {'static': QuickSitemap}}, 
         name='django.contrib.sitemaps.views.sitemap'),
    
    
    path('robots.txt/', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain'
    )),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # For production
    urlpatterns += static('/admin/static/', document_root=os.path.join(settings.BASE_DIR, 'staticfiles/admin'))