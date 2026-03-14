from django.apps import AppConfig


class PortfollioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfollio'
from django.apps import AppConfig

class PortfollioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfollio'

    def ready(self):
        from django.contrib.auth.models import User
        
        if not User.objects.filter(username="Vikas-Dev").exists():
            User.objects.create_superuser(
                username="Vikas-Dev",
                email="your@email.com",
                password="08282007Vk"
            )