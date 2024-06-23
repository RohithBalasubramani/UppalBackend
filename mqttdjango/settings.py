"""
Django settings for mqttdjango project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kv104zat#=gau+udd3240$zcy4yi0q#upy8rb%e1p=ckmnq_uc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "167.71.238.167"]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'rest_framework',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
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

ROOT_URLCONF = 'mqttdjango.urls'

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

WSGI_APPLICATION = 'mqttdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'rohithbalasubramani',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '',
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# If you want to use a dedicated directory for collected static files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


JAZZMIN_SETTINGS = {
    "site_title": "M\u00B2 Tech Hub Admin",
    "site_header": "M\u00B2 Tech Hub Admin",
    "site_brand": "M\u00B2  EMS",
    "site_logo": "assets/logo.png",  # Add your logo path
    "login_logo": "assets/logo_black.png",
    "welcome_sign": "Welcome to the Energy Management Admin Panel of M\u00B2 Tech Hub",
    "show_sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "main"},  # Replace 'main' with the name of your app
    ],
    "usermenu_links": [
        {"name": "Support", "new_window": True},
        {"model": "auth.user"},
    ],
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "vertical_tabs",
        "auth.group": "horizontal_tabs",
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main.skyd1reading": "fas fa-bolt",
        "main.utility1st2ndfs2reading": "fas fa-bolt",
        "main.sparestation3reading": "fas fa-bolt",
        "main.thirdfloorzohos4reading": "fas fa-bolt",
        "main.sixthfloors5reading": "fas fa-bolt",
        "main.spares6reading": "fas fa-bolt",
        "main.spares7reading": "fas fa-bolt",
        "main.thirdfifthfloorkotakreading": "fas fa-bolt",
        "main.dg2s3reading": "fas fa-bolt",
        "main.ebs10reading": "fas fa-bolt",
        "main.apfcs11reading": "fas fa-bolt",
        "main.dg1s12reading": "fas fa-bolt",
        "main.solars13reading": "fas fa-sun",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}
