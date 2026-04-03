import os
import base64
from binascii import Error as BinasciiError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
import django
django.setup()
from django.contrib.sessions.models import Session

bad = []
for s in Session.objects.all():
    try:
        base64.b64decode(s.session_data.encode('ascii'))
    except Exception as e:
        bad.append((s.session_key, str(e)))
        print('Deleting corrupt session:', s.session_key, str(e))
        s.delete()

print('Total deleted corrupt sessions:', len(bad))
