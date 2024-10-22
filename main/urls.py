from django.contrib import admin
from django.urls import path
from . import views  # Ensure you're importing the index view

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('verify/', views.verify_account, name='verify_account') # Use the imported index view here
]
