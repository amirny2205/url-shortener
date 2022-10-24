from .base import *

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

DOMAIN = 'http://localhost/'

ALLOWED_HOSTS = []

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "shortener",
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': "localhost",
        'PORT': 5403,
   }
}
