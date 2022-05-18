from pathlib import Path
import os
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROD_STATUS = os.environ.get("PRODUCTION", False)

# Using the production status of the server to set the DEBUG value 
# (doing it this way because of a qwerk of the django-celery module).
if PROD_STATUS:
    DEBUG=False
else:
    DEBUG=True

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY:
SECRET_KEY = os.environ.get("SECRET_KEY", "test_django_secret_key")

ALLOWED_HOSTS = ["*"]

# Application definition:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party Applications:
    "rest_framework",
    "rest_framework.authtoken",
    "django_celery_beat",
    "djoser",
    "drf_yasg",
    "django_filters",
    "tinymce",
    "crispy_forms",

    # Frontend Application:
    "application_frontend",

    # Core API Logic:   
    "api_core",

    # Project specific API Applications:
    "data_APIs.reddit_api",
    "data_APIs.twitter_api",
    "data_APIs.articles_api"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'private_rest_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, "templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'private_rest_api.wsgi.application'

# REST FRAMEWORK Configuration:
REST_FRAMEWORK = {
    # Authentication/Permission:
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}

# Database
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["POSTGRES_DB"],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': os.environ["POSTGRES_HOST"],
        'PORT': os.environ["POSTGRES_PORT"]
    }
}

# Celery Settings:
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BEAT_SCHEDULE_FILENAME = "celerybeat-schedule"

# Don't use pickle as serializer, json is much safer
CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = os.environ["CELERY_RESULT_BACKEND"]
CELERY_TASK_SERIALIZER = "json"  
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True  
CELERY_TIMEZONE = "UTC"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Sentry Error Catching Configuration (not for ):
"""
# Importing SDK:
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://fe8a2428b4984abd83604d5c26a9c051@o1148429.ingest.sentry.io/6219915",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
"""

# Configuration for Swagger UI:
SWAGGER_SETTINGS = {
    # Token Authorization:
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media Files:
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Frontend styling for TinyMCE:
TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'
TINYMCE_COMPRESSOR = False

# Pointing to the Custom User Model:
AUTH_USER_MODEL = "api_core.CustomUser"

# Login route configs:
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Crispy Forms Configurations:
CRISPY_TEMPLATE_PACK = 'bootstrap4'