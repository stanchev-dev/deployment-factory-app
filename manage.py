#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # смени с твоето
    try:
        from django.core.management import execute_from_command_line

        #  Създаване на суперюзър – само при команда runserver (или migrate)
        if 'runserver' in sys.argv or 'migrate' in sys.argv:
            import django
            django.setup()

            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = 'admin'
            password = 'Test1234!'
            email = 'admin@example.com'

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, password=password, email=email)
                print('✅ Суперюзърът е създаден.')
            else:
                print('ℹ️ Суперюзърът вече съществува.')

        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
