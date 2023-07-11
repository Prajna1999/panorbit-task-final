"""
Django settings for panorbit project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-609kc6n_bzpwrda%tj248swbyb5^v5f1_)#xg%h3d$$z5kqk^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.search.apps.SearchConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
    ]
}




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'panorbit.urls'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#SMTP EMAIL BACKEND SETTING
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gituprajna20@gmail.com'  
EMAIL_HOST_PASSWORD = 'awjfyaprnldutcuk'  

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'panorbit.wsgi.application'
# panorbit-task-final-main/panorbit/settings.py




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'data':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data.sqlite',
    }
}

# class SearchRouter:
#     """
#     A router to control all database operations on models in the
#     search application.
#     """
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'search':
#             return 'data'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'search':
#             return 'data'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label == 'search' or \
#            obj2._meta.app_label == 'search':
#            return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'search':
#             return db == 'data'
#         return None

# DATABASE_ROUTERS = ['panorbit.settings.SearchRouter']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'world',
#         'USER': 'root',
#         'PASSWORD': 'Prajna@1999',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

#custom auth user model
AUTH_USER_MODEL="users.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators



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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



