# -*- coding: utf-8 -*-
"""
Django settings
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vqje&(s$kn!osyitq#y%y1)g7-63#ia#+45(d&c%7x7u)d!pn3'

# SECURITY WARNING: don't run with debug turned on in production!

# PYTHON version
PYTHON_VERSION = sys.version_info

DEBUG_PROPAGATE_EXCEPTIONS = False
DEBUG = DEBUG_PROPAGATE_EXCEPTIONS

ALLOWED_HOSTS = ['settings.py']

# Application definition

INSTALLED_APPS = (
    # 'django_admin_bootstrapped',
    'bedjango_tailor',
    'base',
    'users',
    'tailor',
    'comercial',
    'recrutamento',
    'cachalot',
    'debug_toolbar',
    'material',
    'material.admin',
    'material.frontend',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'rosetta',
    'cookielaw',
)

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': ['../templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.breadcrumbs',
                'base.context_processors.add_login_form'
            ],
            'debug': DEBUG,
        },
    },
]
# WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
}
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=500)

# Cache: http://django-cachalot.readthedocs.io/en/latest/quickstart.html
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHALOT_ENABLED = True
CACHALOT_CACHE = 'default'

# Django toolbar https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'cachalot.panels.CachalotPanel',
]


def show_toolbar(request):
    return DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LOCALE_PATHS = [
    # '/django-app/locale',
    os.path.join(BASE_DIR, 'locale')
]

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'base.validators.CustomPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

LANGUAGES = (
    ('pt-br', 'Português (Brasil)'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

LOGIN_URL = '/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
FIXTURE_DIRS = ('bedjango_tailor/fixtures',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'filipe@tailorit.com.br'
EMAIL_HOST_PASSWORD = 'tailorpwd18'
EMAIL_PORT = 587

# Django registration

ACCOUNT_EMAIL_VERIFICATION = 'none'

# To indicate if the register its open.
REGISTRATION_OPEN = True
# https://django-registration.readthedocs.io/en/2.1.1/settings.html#django.conf.settings.REGISTRATION_OPEN


# Configuring the HMAC activation workflow

# To specify the days that the user must be activate his register.
ACCOUNT_ACTIVATION_DAYS = 1
# https://django-registration.readthedocs.io/en/2.1.1/settings.html#django.conf.settings.ACCOUNT_ACTIVATION_DAYS

# To specify a str to construct the activation code
REGISTRATION_SALT = 'registration'
# https://django-registration.readthedocs.io/en/2.1.1/settings.html#django.conf.settings.REGISTRATION_SALT

# Email config
EMAIL_FROM = 'info@bedjango.com'
EMAIL_TO = 'info@bedjango.com'
