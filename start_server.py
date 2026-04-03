#!/usr/bin/env python
import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Change to the project directory
os.chdir(project_dir)

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

import django
django.setup()

from django.core.management import call_command
call_command('runserver', '0.0.0.0:8000')
