# urls.py

from django.urls import path
from .views import create_profile, view_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', create_profile, name='create'),
    path('profile/', view_profile, name='profile'),

    # Add other URL patterns here
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)