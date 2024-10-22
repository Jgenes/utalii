# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    offices = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    member_of = models.CharField(max_length=255)
    tour_types = models.CharField(max_length=255)
    price_ranges = models.CharField(max_length=255)
    destinations = models.CharField(max_length=255)
    overview = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)  # New field for company name
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.offices} Profile"
