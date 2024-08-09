# settings.py

import os

# Base settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'supersecretkey'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Application definition
INSTALLED_APPS = [
    # Default Django apps
]

MIDDLEWARE = [
    # Default Django middleware
]

ROOT_URLCONF = 'myproject.urls'
TEMPLATES = [
    # Template settings
]
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files configuration
STATIC_URL = '/static/'

# Custom settings
ENABLE_DEBUG = os.getenv('ENABLE_DEBUG', 'False').lower() in ('true', '1', 't')

# Override settings for development
if ENABLE_DEBUG:
    DEBUG = True
    ALLOWED_HOSTS = []
