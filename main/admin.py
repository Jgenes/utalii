from django.contrib import admin
from .models import AccountVerification, UploadedFile

admin.site.register(AccountVerification)
admin.site.register(UploadedFile)