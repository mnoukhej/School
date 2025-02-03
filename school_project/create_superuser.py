import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')
django.setup()

from django.contrib.auth.models import User

# Remove existing superuser if exists
User.objects.filter(username='mnoukhej').delete()
User.objects.filter(username='admin').delete()

# Create new superuser
User.objects.create_superuser('mnoukhej', 'mnoukhej@gmail.com', 'Kolkata@786')
print("Superuser created successfully!")
