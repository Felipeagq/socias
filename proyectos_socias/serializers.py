from dataclasses import field
from rest_framework import serializers
from proyectos_socias.models import Proyectos,Publicaciones

class ProyectosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'


class PublicacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
        fields = '__all__'