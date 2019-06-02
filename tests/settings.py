SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "scrobble_server.core",
    "scrobble_server.api.v12",
    "tests",
]

MIDDLEWARE = []

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

ROOT_URLCONF = "tests.urls"

USE_TZ = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
