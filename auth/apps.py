from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # Folder is `auth` but label must differ from django.contrib.auth
    name = "auth"
    label = "user_auth"
