from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

if eval(os.environ.get('PRODUCTION')): 
    STATIC_URL = "https://%s/%s/" % (os.environ.get('AWS_S3_CUSTOM_DOMAIN'), os.environ.get('AWS_STATIC_LOCATION'))
    DEFAULT_FILE_STORAGE = 'config.custom_storages.MediaStorage'
    STATICFILES_STORAGE = 'config.custom_storages.StaticStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'   
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')