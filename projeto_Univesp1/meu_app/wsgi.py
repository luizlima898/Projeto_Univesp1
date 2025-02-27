import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MUDULE', 'projeto_Univesp1.settings')
application = get_wsgi_application()