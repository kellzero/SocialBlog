)"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'bookstore.settings'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'kellzero.pythonanywhere.com'
os.environ['DEBUG'] = 'False'
os.environ['SECRET_KEY'] = 'sua-chave-secreta-aqui'


from dotenv import load_dotenv

load_dotenv('/home/kellzero/BookStore/.env')

path = '/home/kellzero/BookStore'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
