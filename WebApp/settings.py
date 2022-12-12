
from pathlib import Path
import os
from django.contrib.messages import constants as mesaje_de_error

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--@b7zz!m!gw$04uo58q3jr)g@^g%k0ybrs7(=8lj=y@=mu7cyg'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'ipregister.apps.IpregisterConfig',
    'myportfolio.apps.MyportfolioConfig',
    'autenticacion.apps.AutenticacionConfig',
    'crispy_forms',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'WebApp.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'WebApp.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATES_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    mesaje_de_error.DEBUG: 'debug',
    mesaje_de_error.INFO: 'info',
    mesaje_de_error.SUCCESS: 'success',
    mesaje_de_error.WARNING: 'warning',
    mesaje_de_error.ERROR: 'danger',
}


#FILES
MEDIA_ROOR = os.path.join(BASE_DIR,"media")
MEDIA_URL = '/media/'

# LOGIN
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static')),]
