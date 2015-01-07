"""
Django settings for ianwoolf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#SITE_ROOT=os.path.join(os.path.abspath(os.path.dirname(__file__)),'..')
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ev%^!kbzh(3=xo32t%ydodxk&=^gfxugu_!$u(#@w_5__u9z*u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tt',
    'rest_framework',
)
EST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ianwoolf.urls'

WSGI_APPLICATION = 'ianwoolf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'django',
        'USER': 'root',
        'PORT': 3306,
        'PASSWORD': 'MhxzKhl',
        'TEST_NAME': 'test_huston',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR),'static','templates'),
    #os.path.join('/home/xiaoju/mywork/ianwoolf/static/templates/'),
)
#STATICFILES_DIRS = (
#    (STTATIC_ROOT,
#    ("css", os.path.join(STATIC_ROOT,'css')),
#    ("js", os.path.join(STATIC_ROOT,'js')),
#    ("images", os.path.join(STATIC_ROOT,'images')),
#)
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'bower_components'),
#    os.path.join(BASE_DIR, 'static/staic'),
#os.path.join(os.path.join(os.path.dirname(BASE_DIR), 'static') ))
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'static') 
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'static') 
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'media')
STATICFILES_DIRS =[(
                 os.path.join(os.path.dirname(BASE_DIR),'static_debug/static-only')
                 )]
if  not DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'static-only') 
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static', 'media')
    STATICFILES_DIRS =[(
                      os.path.join(os.path.dirname(BASE_DIR),'static','static')
                      )]    #STATIC_URL
