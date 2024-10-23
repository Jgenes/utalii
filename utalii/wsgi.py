"""
WSGI config for utalii project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/tourTanzania/https://github.com/Jgenes/utalii.git'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'utalii.settings'  # Adjust as necessary

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
