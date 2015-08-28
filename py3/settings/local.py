from py3.settings.common import *

DEBUG = True


ALLOWED_HOSTS = ['localhost']


LOGGING = {
   'version': 1,
   'handlers': {
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
       },
   },
   'loggers': {
       '': {
           'handlers': ['console'],
           'level': 'WARN',
           'propagate': False,
       },
       'django.db.backends': {
           'level': 'WARN',
           'handers': ['console'],
       },
       'sqlalchemy.engine': {
           'level': 'INFO',
           'handers': ['console'],
       },
   },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite_demo'),
    }
}

ALDJEMY_ENGINES = {
    'sqlite3': 'sqlite+pysqlite'
}



