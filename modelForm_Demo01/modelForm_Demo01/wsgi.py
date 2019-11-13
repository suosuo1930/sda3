"""
WSGI config for modelForm_Demo01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import dotenv

dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelForm_Demo01.settings')

application = get_wsgi_application()
