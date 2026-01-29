#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfollio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def create_superuser():
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
                print("✅ Superuser created")
            else:
                print("ℹ️ Superuser already exists")
    except Exception as e:
        print("❌ Superuser creation skipped:", e)

create_superuser()



if __name__ == '__main__':
    main()
