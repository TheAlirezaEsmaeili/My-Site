"""
تنظیمات پروژه ولاگ.
"""
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages_constants

BASE_DIR = Path(__file__).resolve().parent.parent

# --- امنیت ---
# هشدار: قبل از انتشار در محیط عملیاتی، این مقدار را تغییر دهید و مخفی نگه دارید.
SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG",cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=lambda v:[s.strip() for s in v.split(',')],default='*')

# --- اپلیکیشن‌ها ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
    "accounts"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vlogsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "vlogsite.wsgi.application"
ASGI_APPLICATION = "vlogsite.asgi.application"

# --- پایگاه داده ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- اعتبارسنجی رمز عبور ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- زبان و منطقه زمانی ---
LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

# --- فایل‌های استاتیک و رسانه ---
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "blog" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- احراز هویت ---
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# --- پیام‌ها ---
MESSAGE_TAGS = {
    messages_constants.ERROR: "danger",
}

AUTH_USER_MODEL = 'accounts.User'