"""Unitテスト向けのsettingsモジュールです
"""

from curama.settings.common import *
from aldjemy.types import (
    simple,
)
from curama.lib.aldjemy.custom_types import (
    SQLiteDate,
    SQLiteDateTime,
)

# デバッグ設定
DEBUG = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# SQLAlchemyで利用するDB設定
ALDJEMY_ENGINES = {
    'sqlite3': 'sqlite+pysqlite'
}

# DjangoModelのFieldTypeからSQLAlchemyのFieldTypeへ変換定義を一部上書きする設定
# SQLiteにはDate,DateTime型が存在しないため、ORM側でconvert処理を実装します
# (String <--> python's datetime)
# なお、DjangoORM側でDateField型を選択している場合は正常に動作するため、
# ここでの指定は本来DateTimeField型のみでも問題ありません
# おそらくSQLAlchemy側のバグ? 仕様?
# (Python3 SQLAlchemy DateTime型をSQLiteで利用すると値がbytesになる)
ALDJEMY_DATA_TYPES = {
    'DateTimeField': simple(SQLiteDateTime)
}