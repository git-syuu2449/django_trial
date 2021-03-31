'''
開発環境用の設定ファイル
NOTE: ymlかenvで該当箇所だけ切り替えの方がいいかもしれないが、別ファイル化する
'''

import environ

from .base import *

env = environ.Env()
env.read_env(os.path.join(BASE_DIR,'.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

ALLOWED_HOSTS = []


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '88j#_#fr((w8tvvhp@!^3u3r=y+zje-3ukiz4adcy@0nh7ft8a'


INSTALLED_APPS += (
    'debug_toolbar', # and other apps for local development
)


MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'traial',
        'USER':'root',
        'PASSWORD':'Root1234!',
        'HOST':'localhost',
        'PORT':'',
    }
}


INTERNAL_IPS = ['127.0.0.1']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # ログ出力フォーマットの設定
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                    '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    # ハンドラの設定
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'production',
        },
    },
    # ロガーの設定
    'loggers': {
        # 自分で追加したアプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django自身が出力するログ全般を拾うロガー
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}