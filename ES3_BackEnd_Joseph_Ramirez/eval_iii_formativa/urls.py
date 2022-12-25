from django.contrib import admin
from django.urls import path, include
from .views import login, userLogout
#----------------------------[Importaciones]----------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', login),
    path('api/logout/', userLogout),
    path('api/', include('mundial_api.urls')),
    path('app/', include('mundial_app.urls')),
]
