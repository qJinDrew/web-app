from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e$g^xom*yx@iwzw=%8py7v6tsex_nqfirp3mrd(w4d-+olb&3l'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # отображение ошибок на сайте пользователю (True - Да / Folse - нет)

ALLOWED_HOSTS = []  # хост, домен "https:\\.."

# Application definition

INSTALLED_APPS = [  # регистрация приложений
    'main',
    'news',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [  # плагины внутри проекта
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myweb.urls'  # основной файл urls

TEMPLATES = [  # шаблоны
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myweb.wsgi.application'  # при помощи данной технологии мы можем выгрузить наш сайт на сервер

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {  # с какой базой данных мы работаем (SQL)
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'C:/Program Files/PyCharm Community Edition 2023.1/PycharmProjects/web-app/myweb/db.sqlite3',
        'USER': 'admin',
        'PASSWORD': '',
    }
}
# 'NAME': BASE_DIR / 'db.sqlite3',

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# Ниже идет дополнительные переменные, которые дополняют новым функционалом наше приложение, описывает все глобальные
# настройки приложения
LANGUAGE_CODE = 'ru'  # язык для нашего приложения

TIME_ZONE = 'UTC'  # временная зона для нашего приложения

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

""" 
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/news/img')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""

# Изначально было так ..
# STATIC_URL = 'media/'
# STATICFILES_DIRS = [
#    BASE_DIR / "media",
# ]


# Default p
