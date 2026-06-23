from django.apps import AppConfig


class UsersExtensionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bias_ext_users.backend"
    label = "users"
    verbose_name = "Bias Users"

