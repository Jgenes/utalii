from django.db import models
from django.contrib.auth.models import User

class AccountVerification(models.Model):
    operator_name = models.CharField(max_length=255)  # Field for the operator's name
    url = models.URLField()  # Field for a URL
    address = models.TextField()  # Field for the address
    email_verified = models.BooleanField(default=False)  # Email verification status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model

    def __str__(self):
        return self.operator_name

class UploadedFile(models.Model):
    verification_account = models.ForeignKey(
        AccountVerification,
        on_delete=models.CASCADE,
        related_name='uploaded_files'  # Change the related_name here
    )
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
