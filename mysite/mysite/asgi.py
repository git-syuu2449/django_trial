"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import environ

from django.core.asgi import get_asgi_application
from mysite.settings.base import BASE_DIR

# envのDebugによって設定ファイルの切り替えを行う
if env.bool('DEBUG') == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')
elif env.bool('DEBUG') == False:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')

application = get_asgi_application()
