"""
Django settings for makerspaceleiden project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import locale
from moneyed import Money, EUR

os.umask(2)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "6mh_k^thni&-6)!sfz#7i_6i@(6jesl&lrxba)#&nemt-dc0d7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["10.11.0.158", "*"]

# Allow users to create their own entitlement as a one off
# bootstrapping thing.
#
GRAND_AMNESTY = True

# Harsher way to exclude storage module / top level
STORAGE = False
# Application definition

INSTALLED_APPS = [
    "import_export",
    "simple_history",
    "search_admin_autocomplete",
    "qr_code",
    "djmoney",
    "makerspaceleiden",
    "storage.apps.StorageConfig",
    "memberbox.apps.MemberboxConfig",
    "members.apps.UserConfig",
    "acl.apps.AclConfig",
    "selfservice.apps.SelfserviceConfig",
    "kiosk.apps.KioskConfig",
    "ufo.apps.UfoConfig",
    "unknowntags.apps.UnknowntagsConfig",
    "servicelog.apps.ServicelogConfig",
    "mailinglists.apps.MailinglistsConfig",
    "chores.apps.ChoresConfig",
    "mainssensor.apps.MainssensorConfig",
    "kwh.apps.KwhConfig",
    "pettycash.apps.PettycashConfig",
    "ultimaker.apps.UltimakerConfig",
    "spaceapi.apps.SpaceapiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #    'autocomplete_light',
    "django.contrib.sites",
    "revproxy",
]

SITE_ID = 1

MIDDLEWARE = [
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "makerspaceleiden.urls"

TEMPLATE_LOADERS = ("django.template.loaders.app_directories.load_template_source",)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
            ],
        },
    },
]

SETTINGS_EXPORT = [
    "GRAND_AMNESTY",
    "STORAGE",
    "POT_ID",
    "POT_LABEL",
    "NONE_ID",
    "NONE_LABEL",
    "TRUSTEES",
]

WSGI_APPLICATION = "makerspaceleiden.wsgi.application"

MAILINGLIST = "deelnemers@lists.makerspaceleiden.nl"
TRUSTEES = "hetbestuur@lists.makerspaceleiden.nl"

DEFAULT_FROM_EMAIL = "noc@makerspaceleiden.nl"
# Leave it to FORCE_SCRPT do do the psotfix right
BASE = "https://makerspaceleiden.nl"

MSL_USER = 63
SETTINGS_EXPORT.append("MSL_USER")

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

if not os.getenv("LANG"):
    LANG = "en_US.UTF-8"
    os.environ["LANG"] = LANG
    # locale.setlocale(locale.LANG, LANG)

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_TZ = True

# -- START - Custom formatting of date/time and numbers ----
USE_L10N = False

DATETIME_FORMAT = "D Y-m-d G:i:s"
TIME_FORMAT = "G:i:s"
DATE_FORMAT = "D Y-m-d"
SHORT_DATE_FORMAT = "Y-m-d"

YEAR_MONTH_FORMAT = r"Y-m"
MONTH_DAY_FORMAT = r"m-d"
SHORT_DATETIME_FORMAT = "Y-m-d G:i"
FIRST_DAY_OF_WEEK = 1  # Monday

DECIMAL_SEPARATOR = ","
THOUSAND_SEPARATOR = "."
NUMBER_GROUPING = 3
# -- END - Custom formatting of date/time and numbers ----


LOGIN_URL = "/login/"
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []

AUTH_USER_MODEL = "members.User"
MEDIA_URL = "/media/"

MAX_ZIPFILE = 48 * 1024 * 1024
MIN_IMAGE_SIZE = 2 * 1024
MAX_IMAGE_SIZE = 8 * 1024 * 1024
MAX_IMAGE_WIDTH = 1280

from stdimage.validators import MinSizeValidator, MaxSizeValidator

IMG_VALIDATORS = [MinSizeValidator(100, 100), MaxSizeValidator(8000, 8000)]

# Note: the labels are effectively 'hardcoded' in the templates
# and code; the sizes are free to edit.
#
IMG_VARIATIONS = {
    "thumbnail": (100, 100, True),
    "medium": (300, 200),
    "large": (600, 400),
}

UFO_DEADLINE_DAYS = 14
UFO_DISPOSE_DAYS = 7

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    "qr-code": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "qr-code-cache",
        "TIMEOUT": 3600,
    },
}

QR_CODE_CACHE_ALIAS = "qr-code"

# Set to a list to be kept informed of things like UFO
# deadlines and what not.
#
ALSO_INFORM_EMAIL_ADDRESSES = []

# Once a person has this many storage requests - the email
# to the list gets an extra element highlihgting this; with
# a ling to what the person also has in store
STORAGE_HIGHLIGHT_LIMIT = 3

UT_BEARER_SECRET = "not-so-very-secret-127.0.0.1"

# Only show the past 7 days of unknown tags. And up to 10.
#
UT_DAYS_CUTOFF = 7
UT_COUNT_CUTOFF = 10

# Extact spelling as created in 'group' through the /admin/ interface.
SENSOR_USER_GROUP = "mains Sensor Admins"
NETADMIN_USER_GROUP = "network admins"


# REGISTRATION_OPEN = False
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Payment system
#
# When not defined - available all; but listings limited
# will not show people with 0-balance and no transactions
# for PETTYCASH_NOUSE_DAYS
# PETTYCASH_DEMO_USER_GROUP = "pettycash demo group"
PETTYCASH_NOUSE_DAYS = 60
PETTYCASH_ADMIN_GROUP = "pettycash admin group"
PETTYCASH_TREASURER_GROUP = "pettycash admin group"
PETTYCASH_TOPUP = 15
PETTYCASH_TNS = "Stichting Makerspace Leiden"
PETTYCASH_IBAN = "NL18RABO0123459876"
POT_ID = 1
NONE_ID = 217
NONE_LABEL = "Former participant"
POT_LABEL = "Makerspace (de zwarte Pot)"
CURRENCIES = ["EUR"]

MAX_PAY_API = Money(10.00, EUR)
MAX_PAY_DEPOSITI = Money(100.00, EUR)
MAX_PAY_REIMBURSE = Money(100.00, EUR)
PAY_MAXNONCE_AGE_MINUTES = 20

# Days and max number of unknown terminals to keep.
# (accepted number of terminals is unconstrained) - this
# is just for the short period between booting one for
# the first time and pairing it. Once we hit MAX
# bring it back to MIN.
#
PETTYCASH_TERMS_MAX_UNKNOWN = 4
PETTYCASH_TERMS_MIN_UNKNOWN = 1
PETTYCASH_TERMS_MINS_CUTOFF = 10

try:
    from .local import *
except ImportError:
    print(
        "WARNING -- no local configs. You propably want to copy makerspaceleiden/debug.py to local.py & tweak it !!"
    )
    pass
