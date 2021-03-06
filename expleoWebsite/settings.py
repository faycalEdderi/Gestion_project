"""
Django settings for expleoWebsite project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')


MESSAGE_TAGS = {
    messages.SUCCESS: 'alert alert-success',
    messages.ERROR: 'alert alert-danger',
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9&4nmeg%dupx=sc*2^-5#e1j-pc^grc%up1&551++pv67e&-fm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'django_cleanup.apps.CleanupConfig',
    'profil.apps.ProfilConfig',
    'uos.apps.UosConfig',
    'automatic.apps.AutomaticConfig',
    'send_mail.apps.SendMailConfig',


    'import_export',
    
    
]
IMPORT_EXPORT_USE_TRANSACTIONS = True
CRONJOBS=[
    ('*/5****',
    'expleowebsite.automatic.my_scheduled_job')
]
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = "amqp"
CELERY_ACCEPT_CONTENT =['json']
CELERY_TASK_SERIALIZE = 'json'
CELERY_RESULT_SERIALIZE = 'json'
CELERY_AMQP_TASK_RESULT_EXPIRES = 1000

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'profil.views.LoginRequiredMiddleware',
]


ROOT_URLCONF = 'expleoWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'expleoWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'profile_pic/photo')

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

LOGOUT_REDIRECT_URL = "connexion"
LOGIN_URL = "connexion"


#Rediriger vers la class EmailBackend (qui permet de se connecter avc sont adersse mail)
AUTHENTICATION_BACKENDS = (
    'profil.backends.EmailBackend', 
)


# Ci Dessous parametres permettant la reception de mail via le shell 
# ecrire la cmd dans un nouveau shell : python -m smtpd -n -c DebuggingServer localhost:1025 
# si rien ne s'affiche c'est normal il faut d'abord envoy?? l'email.
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

#Ces fichier stock dans le dossier "sent_emails" tous les email envoy?? a partir de django

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend" # During development only
#EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

# Il faut parametrer une adresse mail professionel avec les parametres suivant pour envoyer un "vrai" mail
# EMAIL_HOST
# EMAIL_PORT
# EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD
# EMAIL_USES_TLS
# EMAIL_USE_SSL






EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'expleowebsite@gmail.com'
EMAIL_HOST_PASSWORD = 'Faycal.78'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

