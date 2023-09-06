# Django-DRF-Boilerplate

A powerful Django and Django REST Framework boilerplate project that provides a solid foundation for building web applications with essential features and best practices of class-based views.
<br/>
Minimal front-end has also been implemented in HTML, CSS and bootstrap for front-end testing.
<hr/>

## Features

- [Custom User Model](#custom-user-model)
  - [Email-Based Authentication](#custom-user-model)
- [Authentication via Social Account](#authentication-via-social-account)
- [JWT Authentication](#jwt-authentication)
- [Account Activation](#account-activation)
- [Password Management](#password-management)
  - [Reset Password via Email](#password-management)
  - [Change Password using old password](#password-management)
- [Profile Section](#profile-section)
<hr/>

### Custom User Model

The default user model has been customized to exclude username and enforce email-based authentication, and it can be further customized to one's need. Add following lines in `settings.py` to use the custom model.

```py
AUTH_USER_MODEL = 'users.CustomUser'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
```
<hr/>

### Authentication via Social Account

For authentication via social accounts (Google and GitHub in this project) `django-allauth` is used. Add following apps in `INSTALLED_APPS` in `settings.py` to use `django-allauth` in your project and specify authentication backend.

```py
INSTALLED_APPS = [
    # Other apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
```

Define the scope and login redirect URL by adding following lines in `settings.py`.

```py
SOCIAL_ACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        }
    }
}

LOGIN_REDIRECT_URL = '/'
```

To connect social account of users already signed-up with the specified email rather than creating a new user, a custom adapter is used. Specify the path by adding following line in `settings.py`.

```py
SOCIALACCOUNT_ADAPTER = 'users.allauth.adapters.CustomSocialAccountAdapter'
```
<hr/>

### JWT Authentication

Simple JWT has been used for JSON Web Token authentication backend for the Django REST Framework.

```py
INSTALLED_APPS = [
    # Other apps
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

Specify the lifetime of the tokens.

```py
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```
<hr/>

### Account Activation

Activation via email has been integrated in the project. Set up `SMTP` server by adding following lines in `settings.py` to send email.

```py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'email host user'
EMAIL_HOST_PASSWORD = 'email host password'
```
<hr/>

### Password Management

- Reset Password via Email

A reset link is sent to the user email address using the same `SMTP` server that we set up in the [previous step](#account-activation). Specify the duration of the link by adding following line in `settings.py`.

```py
PASSWORD_RESET_TIMEOUT = 7200  # 2 hour
```

- Change Password using Old Password

Changing the user password using old password has been implemented as well.
<hr/>

### Profile Section

User Profile section has also been implemented where users can edit their profile or look at others' profile via user handle.
<hr/>

## Connect PostgreSQL

We'll be using PostgreSQL for database management instead of django's built-in sqlite3.

```py
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'database name',
       'USER': 'user associated with db',
       'PASSWORD': 'password',
       'HOST': 'host',
       'PORT': 'port',
   }
}
```
<hr/>

## Getting Started

Follow these steps to set up and run the project locally:

- Clone the repo

```commandline
git clone https://github.com/Fahad-Habib/Django-DRF-Boilerplate.git
cd Django-DRF-Boilerplate
```

- Install requirements

```commandline
python -m pip install -r requirements.txt
```

- Set up environment

Create a `.env` file in `boilerplate` directory following `sample.env`

- Run migrations

```commandline
python manage.py migrate
```

- Start the server

```commandline
python manage.py runserver
```
