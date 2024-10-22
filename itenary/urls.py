from django.contrib import admin
from django.urls import path, include  # Make sure path and include are imported
from . import views

urlpatterns = [
    path('', views.itenary_list, name='list'),  # Default path for itenary list view
    # Include the userAuth URLs
]
