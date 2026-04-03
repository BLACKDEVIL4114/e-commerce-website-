import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

User = get_user_model()
username = 'henil'
email = 'henil@example.com'
password ='henil1234'

if User.objects.filter(username=username).exists():
    print('superuser_exists')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print('superuser_created')
    # For security, do not print the password in logs in real projects.
    print('credentials: username=%s email=%s password=%s' % (username, email, password))
