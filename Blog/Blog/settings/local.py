from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('django_extensions')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
