import environ  
from django.contrib import messages
from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(ENV_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c*(vle^ca^x!rthn-=-d#ui!0s(h$x6__@-p$p5rwthyirg+5b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'mathfilters',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_email_verification',
    'django_google_fonts',
    'sorl.thumbnail',
    'django_celery_beat',
    'django_celery_results',
    "django_htmx",
    'rest_framework',
    'djoser',
    'drf_yasg',

    # apps
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'account.apps.AccountConfig',
    'payment.apps.PaymentConfig',
    'recommend.apps.RecommendConfig',
    'api.apps.ApiConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bigcorp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'bigcorp' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #custom context processors
                'shop.context_processors.categories',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'bigcorp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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


# Project settings
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

APPEND_SLASH = True

# Static files 
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'bigcorp' / 'static',
]

MEDIA_URL = '/media/'   
MEDIA_ROOT = BASE_DIR / 'media'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

# Crispy forms  
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'


def email_verified_callback(user):
    user.is_active = True


# def password_change_callback(user, password):
#     user.set_password(password)


# Global Package Settings
EMAIL_FROM_ADDRESS = 'molokoedovmp@gmail.com'  # mandatory
EMAIL_PAGE_DOMAIN = 'http://127.0.0.1:8000/'  # mandatory (unless you use a custom link)
EMAIL_MULTI_USER = False  # optional (defaults to False)

# Email Verification Settings (mandatory for email sending)
EMAIL_MAIL_SUBJECT = 'Confirm your email {{ user.username }}'
EMAIL_MAIL_HTML = 'account/email/mail_body.html'
EMAIL_MAIL_PLAIN = 'account/email/mail_body.txt'
EMAIL_MAIL_TOKEN_LIFE = 60 * 60  # one hour

# Email Verification Settings (mandatory for builtin view)
EMAIL_MAIL_PAGE_TEMPLATE = 'account/email/email_success_template.html'
EMAIL_MAIL_CALLBACK = email_verified_callback

# Password Recovery Settings (mandatory for email sending)
# EMAIL_PASSWORD_SUBJECT = 'Change your password {{ user.username }}'
# EMAIL_PASSWORD_HTML = 'password_body.html'
# EMAIL_PASSWORD_PLAIN = 'password_body.txt'
# EMAIL_PASSWORD_TOKEN_LIFE = 60 * 10  # 10 minutes

# Password Recovery Settings (mandatory for builtin view)
# EMAIL_PASSWORD_PAGE_TEMPLATE = 'password_changed_template.html'
# EMAIL_PASSWORD_CHANGE_PAGE_TEMPLATE = 'password_change_template.html'
# EMAIL_PASSWORD_CALLBACK = password_change_callback


# For Django Email Backend
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'molokoedovmp@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # os.environ['tflr igmg degm encx'] suggested
EMAIL_USE_TLS = True

#Stripe
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_API_VERSION = env('STRIPE_API_VERSION')

# Yookassa
YOOKASSA_SECRET_KEY = env('YOOKASSA_SECRET_KEY')
YOOKASSA_SHOP_ID = env('YOOKASSA_SHOP_ID')

GOOGLE_FONTS=['Montserrat:wight@300,400', 'Roboto']
GOOGLE_FONTS_DIR = BASE_DIR / 'static'

#Celery
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXTENDED = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "api.permissions.IsAdminOrReadOnly",
    ],
    "DEFAULT_PAGINATION_CLASS": "api.pagination.StandardResultsSetPagination",
    "PAGE_SIZE": 15,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "user_create": "api.serializers.CustomUserCreateSerializer",
    },
    'AUTH_HEADER_TYPES': ('JWT',),

}
