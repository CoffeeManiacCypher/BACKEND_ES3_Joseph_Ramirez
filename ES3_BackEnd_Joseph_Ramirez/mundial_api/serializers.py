from rest_framework import serializers
from mundial_api.models import Equipo, Jugador
#----------------------------[Importaciones]----------------------------

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'        