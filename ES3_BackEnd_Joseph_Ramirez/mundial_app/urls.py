from django.urls import path
from mundial_app import views

#----------------------------[Importaciones]----------------------------

urlpatterns = [
    path('equipo/<int:id>', views.mostrarEquipo),
    path('equipo', views.mostrarEquipos)
]