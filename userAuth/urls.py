from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Correctly defined signup URL
    path('signin/', views.signin, name='signin'),  # Correctly defined signup URL

]
