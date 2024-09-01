from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auth_field = "django.db.models.BigAutoField"
    name = "crmApp"
