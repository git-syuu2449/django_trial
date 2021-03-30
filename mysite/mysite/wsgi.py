"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import environ

from django.core.wsgi import get_wsgi_application
from mysite.settings.base import BASE_DIR

env = environ.Env()
env.read_env(os.path.join(BASE_DIR,'.env'))

# envのDebugによって設定ファイルの切り替えを行う
if env.bool('DEBUG') == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')
elif env.bool('DEBUG') == False:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')

application = get_wsgi_application()
