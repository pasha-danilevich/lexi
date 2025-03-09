from config.base import BASE_PATH

from config.app import get_api_settings, get_app_use_settings
from config.db import get_postgres_settings

api = get_api_settings()
app_use = get_app_use_settings()
db = get_postgres_settings()
