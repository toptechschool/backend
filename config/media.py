from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get('DEBUG')

if DEBUG: 
    STATIC_URL = '/static/'
else:
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    DEFAULT_FILE_STORAGE = 'config.custom_storages.MediaStorage'
    STATICFILES_STORAGE = 'config.custom_storages.StaticStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'   
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_root'), ]