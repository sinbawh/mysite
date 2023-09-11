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



#=-----------------------------

#sites framework
SITE_ID = 3



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thesinab_travel',
        'USER': 'thesinab_sina',
        'PASSWORD': 'Sina2001Bahmani',
        'HOST': 'localhost',  # or the hostname where your MySQL server is running
        'PORT': '3306',      # or the port on which your MySQL server is listening
    }
}
STATICFILES_FINDERS=[
    'compressor.finders.CompressorFinder'
]

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR /'media'

STATICFILES_DIRS = [BASE_DIR /"statics"]
## X-Frame-Options

X_FRAME_OPTIONS = 'SAMEORIGIN'

#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'


# Enable compressor
COMPRESS_ENABLED = True

# Define the URL where compressed files will be served from
COMPRESS_URL = '/static/'

# Define the directory where compressed files will be stored
COMPRESS_ROOT = 'static_root/'

# Specify which file types should be compressed
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-sass', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

#-------------------------------------------------------------------

MAINTENANCE_MODE = True