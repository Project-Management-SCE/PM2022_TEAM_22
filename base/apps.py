from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"

    def ready(self):
        from django.contrib.auth.models import Group
        from dotenv import load_dotenv

        # test

        load_dotenv()
        Group.objects.get_or_create(name="vip")
        Group.objects.get_or_create(name="platinum")
