from .settings import *

DEBUG = True

# Secret Key
SECRET_KEY = '@YJyv\36,(}d6PtglJ"`hdstY]18tj>$Tx+1EX5`*=$3Cd]R?'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['127.0.0.1']