from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('accounts/', include('accounts.urls')),
    path('', include('shop.urls')),

    # Static Pages
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('faq/', TemplateView.as_view(template_name="faq.html"), name='faq'),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name='terms'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)