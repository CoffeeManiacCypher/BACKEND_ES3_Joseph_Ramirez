import os
from django.core.asgi import get_asgi_application
#----------------------------[Importaciones]----------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eval_iii_formativa.settings')

application = get_asgi_application()
