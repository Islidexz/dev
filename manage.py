import os
import sys

if __name__ == '__main__':
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
    if os.getenv('HTTPS') == 'on':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)