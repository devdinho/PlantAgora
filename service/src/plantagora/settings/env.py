from plantagora.settings.base import *
from dotenv import load_dotenv
import os

SITE_ID = 1

load_dotenv(override=True)

DEBUG = os.getenv("DEBUG")

POSTGRES_DB = "plantagora_db"
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = "plantagora_db"

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8001", "http://0.0.0.0:8001"]

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": DB_HOST,
        "PORT": "5432",
    }
}
