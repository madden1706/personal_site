#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    current_env = os.environ['DJANGO_ENV']
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"madresearchden.settings.{current_env}}")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
