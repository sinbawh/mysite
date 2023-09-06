from mysite.settings import *

#=-----------------------------
#dev

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e!3)0_%dtx_3ygcf(e5x579ye71w+gf^v3fqak2r+5-+xcov0f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['thesinabahmani.ir' , 'wwww.thesinabahmani.ir']

CSRF_COOKIE_SECURE = True
from mysite.settings import *

#=-----------------------------

#sites framework
SITE_ID = 2



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR /'media'

STATICFILES_DIRS = [BASE_DIR /"statics"]

X_FRAME_OPTIONS = 'SAMEORIGIN'