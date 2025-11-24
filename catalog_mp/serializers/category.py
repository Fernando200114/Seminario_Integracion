from rest_framework import serializers
from catalog.models import CategoriaVuelo

class CategoriaVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVuelo
        fields = ("id", "nombre", "descripcion", "creado_en", "actualizado_en")
        read_only_fields = ("id", "creado_en", "actualizado_en")
