from .settings import *

DEBUG = True

# Secret Key
SECRET_KEY = 'zil5C~!:_1-3d4FZ;eZL$@8*]P&dd;xW<}A,(7xBNe!ob0?Dl'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['127.0.0.1']       