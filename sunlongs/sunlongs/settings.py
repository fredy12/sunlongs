"""
Django settings for sunlongs project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#e0hf%6hodt$l-isi8g7s_z5_8bbpqjv8dkoe_8d6%%rmyl$l7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'mainsite',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'log_request_id.middleware.RequestIDMiddleware',
)

ROOT_URLCONF = 'sunlongs.urls'

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

WSGI_APPLICATION = 'sunlongs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sunlongs.sqlite3'),
    }
}


#######
# LOG #
#######

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] [%(levelname)s] [%(request_id)s] [%(filename)s:%(lineno)d] - %(message)s",
            'datefmt' : "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'filters': ['request_id'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'sunlongs.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
            'formatter': 'verbose',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'maxBytes': 1024 * 1024 * 100,
#             'backupCount': 30,
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'WARNING',
        },
        'mainsite': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

# end log


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/')+'/'

LOGIN_URL = '/admin/login.html'

############
# SESSIONS #
############

SESSION_COOKIE_AGE = 60 * 60 * 10
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# end session

##########
# EMAILS #
##########

EMAIL_HOST = 'smtp.xxx.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxxxx@xxx.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxx'
EMAIL_USE_TLS = True
EMAIL_FROM_USER = 'xxxxxx@xxx.com'
EMAIL_TO_USER = 'xxx@xxxxx.com'

# end email

##############
# LOGIN INFO #
##############

USER_NAME = 'xxxxx'
USER_EMAIL = 'xxxx@xxxxxx.com'
RESET_PASSWORD_MD5 = 'xxxxxxxxxxxxxx'

# end login info


############
# memcache #
############

MEMCACHE_HOST = '127.0.0.1:11211'
COUNTER_KEY = 'page_counter'

# end memcache
