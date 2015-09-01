from py3.settings.common import *
from aldjemy.types import (
    simple,
)

DEBUG = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ALDJEMY_ENGINES = {
    'sqlite3': 'sqlite+pysqlite'
}