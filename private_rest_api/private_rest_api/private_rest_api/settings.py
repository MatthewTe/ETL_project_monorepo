from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#DEBUG = os.environ.get("DEBUG", True)

#DEBUG=False
DEBUG=True

BASE_DIR = Path(__file__).resolve().parent.parent

if DEBUG:
    SECRET_KEY = '=ku2)(%oeuqzgy=pc3jw8gj+))0t_cpu-9pmjy2hl+$6^jq5t_'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

# Configuring the Settings Params based on the Debug status to seperate between production and development:

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["rest-api"]

# Application definition
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

    # Core API Logic:   
    "api_core",

    # Reddit API:
    "data_APIs.reddit_api"
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
        'DIRS': [],
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
if DEBUG:
    REST_FRAMEWORK = {
        # Authentication/Permission:
        'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
        #'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],

        "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",

        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 10
    }
else:
    REST_FRAMEWORK = {        
        #"DEFAULT_AUTHENTICATION_CLASSES": [
        #    "rest_framework.authentication.BasicAuthentication"
        #    "rest_framework.authentication.SessionAuthentication",
        #    "rest_framework.authentication.TokenAuthentication"],

        "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",

        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        "PAGE_SIZE": 30
    }

# Database
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ["POSTGRES_DB"],
            'USER': os.environ["POSTGRES_USER"],
            'PASSWORD': os.environ["POSTGRES_PASSWORD"],
            'HOST': "rest-api-psql",
            'PORT': os.environ["POSTGRES_PORT"]
        }
    }

if DEBUG:
    pass
else:
    # Configuring the Celery Broker:
    CELERY_BROKER_URL = 'redis://redis:6379/0'

# Celery Settings:
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = "/staticroot/"
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Pointing to the Custom User Model:
AUTH_USER_MODEL = "api_core.CustomUser"