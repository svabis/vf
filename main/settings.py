"""
Django settings for main project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+t%cc5jq-rg+=#9%(qzer83=dwv1$u@oplo*1@+cmc3_^*-ag4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nodarb',
    'klienti',
    'grafiks',
    'pieraksts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                '/home/vfab/templates',
                '/home/vfab/pieraksts/templates',
#                '/home/web/login/template',
#                '/home/web/jobs/template',
#                '/home/web/smhouse/template',
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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vfabrika',
#        'USER': 'django',
        'USER': 'root',
#        'PASSWORD': 'Dj2ng0',
        'PASSWORD': 'Lauma',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


LANGUAGE_CODE = 'LV-LV.UTF-8'

TIME_ZONE = 'EET'
#TIME_ZONE = 'Europe/Riga'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = "/var/www/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/web/static/',
    '/var/www/static/',
)

#STATIC_ROOT = '/home/svabis/web/static/'
#STATIC_ROOT = '/kuvalda/static/'
STATIC_URL = '/static/'

#MEDIA_ROOT = '/home/svabis/web/media/'
MEDIA_ROOT = '/home/vfab/media/'
MEDIA_URL = '/media/'
