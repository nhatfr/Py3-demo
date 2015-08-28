from py3.settings.common import *
from aldjemy.types import (
    simple,
)
from py3.lib.aldjemy.custom_types import (
    SQLiteDate,
    SQLiteDateTime,
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

ALDJEMY_DATA_TYPES = {
    'DateTimeField': simple(SQLiteDateTime)
}