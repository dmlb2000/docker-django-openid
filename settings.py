# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'c14d549c574e4d8cf162404ef0b04598'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'provider_app',
    'oidc_provider',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'provider_app.urls'

WSGI_APPLICATION = 'provider_app.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_ENV_MYSQL_DATABASE'),
        'USER': os.getenv('MYSQL_ENV_MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_ENV_MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
        'PORT': os.getenv('MYSQL_PORT_3306_TCP_PORT'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Custom settings

LOGIN_REDIRECT_URL = '/'


# OIDC Provider settings

SITE_URL = os.getenv('SITE_URL')
OIDC_RSA_KEY_FOLDER = BASE_DIR
