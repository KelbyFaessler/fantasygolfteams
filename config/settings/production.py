import dj_database_url

from .base import *

env = environ.Env()

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['.fantasygolfteams.com'])

MIDDLEWARE = []
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# http://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DATABASES = {}
# The following line automatically uses the 'DATABASE_URL' environment variable
# see https://pypi.org/project/dj-database-url/ for more info
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

DEBUG = True