from .settings import *

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR+'/stats', 'webpack-stats.prod.json'),
        }
}