from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group

    Group.objects.get_or_create(name="vip")
    Group.objects.get_or_create(name="platinum")


class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"

    def ready(self):
        from dotenv import load_dotenv

        post_migrate.connect(create_groups, sender=self)
        load_dotenv()
