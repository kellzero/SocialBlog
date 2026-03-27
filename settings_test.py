# settings_test.py
from bookstore.settings import *

# Chave secreta para testes
SECRET_KEY = 'django-insecure-test-key-1234567890!@#$%^&*()'

# Configurações para testes
DEBUG = True

# Usa SQLite em memória para testes mais rápidos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Garante que o MessageMiddleware está presente
# Se você modificou o MIDDLEWARE no settings original, adicione-o de volta
if 'django.contrib.messages.middleware.MessageMiddleware' not in MIDDLEWARE:
    # Adiciona antes do último middleware (geralmente o SecurityMiddleware)
    MIDDLEWARE.insert(-1, 'django.contrib.messages.middleware.MessageMiddleware')

# Se você removeu o messages nos INSTALLED_APPS, adicione de volta
if 'django.contrib.messages' not in INSTALLED_APPS:
    INSTALLED_APPS.append('django.contrib.messages')

# Configuração de storage para messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'