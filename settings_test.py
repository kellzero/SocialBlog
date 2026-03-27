# bookstore/settings_test.py (ou onde estiver seu settings.py)
from bookstore.settings import *

# Chave secreta para testes
SECRET_KEY = 'django-insecure-test-key-1234567890!@#$%^&*()'

# Desativa mensagens de segurança para testes
DEBUG = True

# Usa SQLite em memória para testes mais rápidos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Desativa o middleware de mensagens para evitar problemas
MIDDLEWARE = [m for m in MIDDLEWARE if 'messages' not in m]

# Se tiver autenticação, pode adicionar:
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]