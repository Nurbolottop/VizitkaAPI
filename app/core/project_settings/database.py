# Database
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('POSTGRES_DB', 'vizitka_db'),
#         'USER': os.getenv('POSTGRES_USER',  'vizitka_db_user'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'nurbo_vizitka'),
#         'HOST': os.getenv('POSTGRES_HOST','db_vizitka_api'),
#         'PORT': os.getenv('POSTGRES_PORT', '5432'),
#     }
# }
