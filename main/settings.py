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
#DEBUG = True
DEBUG = False

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
#    'statistika',
    'django_cleanup',
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
#                '/pieraksts_web/templates',
#                '/pieraksts_web/pieraksts/templates',
#                '/pieraksts_web/grafiks/templates',
                '/home/svabis/pieraksts_web/templates',
                '/home/svabis/pieraksts_web/pieraksts/templates',
                '/home/svabis/pieraksts_web/grafiks/templates',
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

#        'NAME': 'pieraksts',
#        'USER': 'pieraksts',
#        'PASSWORD': 'VFabrika2017',

        'NAME': 'test_pieraksts',
        'USER': 'root',
        'PASSWORD': 'hlu8Jmhq',

        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


#LANGUAGE_CODE = 'LV-LV.UTF-8'
LANGUAGE_CODE = 'LV-LV'

TIME_ZONE = 'EET'
#TIME_ZONE = 'Europe/Riga'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#    '/pieraksts_web/static/',
#)

STATIC_ROOT = "/pieraksts_web/static/"
STATIC_URL = '/static/'

MEDIA_ROOT = '/pieraksts_web/media/'
MEDIA_URL = '/media/'
