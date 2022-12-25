import os
from django.core.wsgi import get_wsgi_application
#----------------------------[Importaciones]----------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eval_iii_formativa.settings')

application = get_wsgi_application()
