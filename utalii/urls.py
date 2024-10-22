from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('main.urls')),  # Main app URL (if applicable)
    path('auth/', include('userAuth.urls')),
    path('itenary/', include('itenary.urls')),  
    path('operators/', include('operators.urls'))# Include the userAuth URLs
]
