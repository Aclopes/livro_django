from .settings import *

DEBUG = True

# Secret Key
SECRET_KEY = 'gy4lynBP22W0HwnX"avCz4+5I-MK`CG{[.!Gnm4wO~k4;lDx9;'

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ALLOWED_HOSTS = ['*'] everything, not safe
# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.149']