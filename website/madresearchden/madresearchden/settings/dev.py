from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y5vsuw(n&ov!-+w8acs=#%g**$_#z2d#0sclbub)lpvo6)7!-s'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split('|')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
