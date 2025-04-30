import os

from dotenv import load_dotenv

from plantagora.settings.base import *

SITE_ID = 1

load_dotenv(override=True)

DEBUG = os.getenv("DEBUG")

POSTGRES_DB = "plantagora_db"
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = "plantagora_db"
DB_PORT = os.getenv("DB_PORT")

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
        "PORT": DB_PORT,
    }
}
