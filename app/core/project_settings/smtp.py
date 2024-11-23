#SMTP SETTINGS
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_USE_TLS = True  # Использовать TLS для защищенного соединения
EMAIL_HOST = 'smtp.gmail.com'  # Адрес SMTP сервера Gmail
EMAIL_PORT = 587  # Порт для подключения к SMTP серверу Gmail
EMAIL_HOST_USER = 'erk1nbaevw2711@gmail.com'
EMAIL_HOST_PASSWORD = 'nthgkaruqpqqhsey'
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
