import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import MEDIA_URL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '47$zr7xqg8ftu@heu^vb55f#@i@azj5l=d1f(!r%l#y4(2cy#&'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'proteinreader.bioinfo.pbf.hr']

INTERNAL_IPS = ['127.0.0.1']  # for debugurl

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    'bootstrap4',
    'crispy_forms',
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'global_login_required.GlobalLoginRequiredMiddleware',  # Require login for everyone
]

ROOT_URLCONF = 'UMCGMicrobiomeWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'UMCGMicrobiomeWeb.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False  # locale ima prednost za dateformat

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

# https://django-glrm.readthedocs.io/en/latest/readme.html#public-views
PUBLIC_VIEWS = [
    'django.contrib.auth.views.LoginView',
    'django.contrib.auth.views.LogoutView',
    # 'django.contrib.auth.views.Pass',
]
PUBLIC_PATHS = [
    # '^%s.*' % MEDIA_URL,  # allow public access to any media on your application
    r'^/accounts/.*',  # allow public access to all django-allauth views
]

AUTH_USER_MODEL = 'app.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

DATE_INPUT_FORMATS = ['%d.%m.%Y']
DATE_FORMAT = 'd.m.Y'




