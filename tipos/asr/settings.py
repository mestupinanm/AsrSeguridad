"""
Django settings for asr project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'svm_)tpa-o^gkn@81sel&lapq2jc7^^-n9c+4y&f9rymz$kum_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tipos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'asr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'asr', 'templates')],
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


WSGI_APPLICATION = 'asr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('TIPOS_DB_NAME', 'tipos_db'),
        'USER': os.environ.get('TIPOS_DB_USER', 'tipos_user'),
        'PASSWORD': os.environ.get('TIPOS_DB_PASSWORD', 'isis2503'),
        'HOST': os.environ.get('TIPOS_DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://dev-y3pgtndrb2bzg280.us.auth0.com/v2/logout?returnTo=http%3A%2F%2Fip_publica_instancia:8000"

SOCIAL_AUTH_TRAILING_SLASH = False  # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'ddev-y3pgtndrb2bzg280.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '0inLmXqscP7oEIVjpXcn5m4egeWLnilY'
SOCIAL_AUTH_AUTH0_SECRET = 'WUrt4ODQ6mYK4fuv3S7M84lR5zVfBqNoX1UWS5xpHWVW4kJrUskkWQKntn0SJzpL'

SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email',
    'role',
]

AUTHENTICATION_BACKENDS = {
    'monitoring.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend',
}
