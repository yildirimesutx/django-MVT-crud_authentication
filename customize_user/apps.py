from django.apps import AppConfig


class CustomizeUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customize_user'
