"""
ASGI config for school_project project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')

application = get_asgi_application()
