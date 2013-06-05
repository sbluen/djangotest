#!/usr/bin/env python
"""A script to assist in the management of the application."""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
