# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from typing import Dict, Tuple, List  # noqa
import dj_database_url
import os
import environ
import logging

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ''),
    SITE_URL=(str, ''),
    APP_NAME=(str, ''),
    EMAIL_BACKEND=(str, 'django.core.mail.backends.console.EmailBackend'),
    EMAIL_HOST=(str, 'localhost'),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    EMAIL_PORT=(int, 25),
    EMAIL_USE_TLS=(bool, False),
    DEFAULT_FROM_EMAIL=(str, ''),
    AWS_S3_CUSTOM_DOMAIN=(str, ''),
    TEST_RUNNER=(str, 'django.test.runner.DiscoverRunner'),
    IN_TEST=(bool, False),
    ALLOW_WEAK_PASSWORDS=(bool, False),
    SECURE_SSL_REDIRECT=(bool, False),
    ENFORCE_HOST=(list, ''),
    RAVEN_DSN=(str, ''),
    SECRET_KEY=(str, ''),
    DATABASE_URL=(str, ''),
    USER=(str, ''),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

SITE_URL = env('SITE_URL')

APP_NAME = env('APP_NAME')

if 'ENFORCE_HOST' in os.environ:
    ENFORCE_HOST = env('ENFORCE_HOST')

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',

    'rest_auth.registration',
    'allauth.account',

    'django_dbq',
    'raven.contrib.django.raven_compat',

    'project.accounts',
    'project.common',
]  # type: List[str]

MIDDLEWARE = [
    'enforce_host.EnforceHostMiddleware',
    'log_request_id.middleware.RequestIDMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be below SecurityMiddleware but above everything else.
]  # type: List[str]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=300
    )
}

# Make all requests atomic
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')


# ThumborStorage settings
IMAGESERVICEURL = os.environ.get('IMAGESERVICEURL', 'https://images.dabdev.net')
IMAGESERVICEKEY = os.environ.get('IMAGESERVICEKEY', '')

# Settings for thumbor storage backend
THUMBOR_SERVER = IMAGESERVICEURL
THUMBOR_SECURITY_KEY = IMAGESERVICEKEY
THUMBOR_RW_SERVER = IMAGESERVICEURL


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "build"),
)


STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # set to 'none' if not required
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'

LOGIN_URL = '/'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

OLD_PASSWORD_FIELD_ENABLED = True

SITE_ID = 1

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
    
        'rest_framework.authentication.SessionAuthentication',
    ),
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'project.accounts.serializers.RegistrationSerializer',
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if env('ALLOW_WEAK_PASSWORDS'):
    AUTH_PASSWORD_VALIDATORS = []

# If s3 django-storages is used, use this host instead of
# amazon (useful for fake-s3 testing)
if env('AWS_S3_CUSTOM_DOMAIN'):
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')

# django-db-queue
JOBS = {
    # Example task
    #    'send_mail': {
    #        'tasks': ['project.email.tasks.send_mail'],
    #    },
}  # type: Dict

TEST_RUNNER = env('TEST_RUNNER')

if env('IN_TEST'):
    logging.disable(logging.ERROR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': 'at=%(levelname)s request_id=%(request_id)s logger=%(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': ['request_id'],
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'log_request_id.middleware': {
            'level': 'INFO',
            'propagate': True,
        },
        'project': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django_dbq': {
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}  # type: Dict

LOG_REQUEST_ID_HEADER = 'HTTP_X_REQUEST_ID'
LOG_REQUESTS = True

RAVEN_DSN = env('RAVEN_DSN')
if RAVEN_DSN:
    # Configure the raven sentry client.
    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN,
    }

    # Capture all error messages and pass them to the sentry logging handler.
    LOGGING['root']['handlers'] += ['sentry']

    # Add the logging handler for sentry.
    LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    }

    # Capture anything emitted by raven/sentry for our log files.
    LOGGING['loggers']['raven'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False,
    }
    LOGGING['loggers']['sentry.errors'] = {
        'level': 'DEBUG',
        'handlers': ['console'],
        'propagate': False,
    }
