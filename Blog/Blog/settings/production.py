from .base import *

ALLOWED_HOSTS = env('ALLOWED_HOSTS', '*').split(',')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
