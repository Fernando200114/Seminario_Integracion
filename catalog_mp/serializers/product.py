from rest_framework import serializers
from catalog.models import Vuelo, CategoriaVuelo

class VueloSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.ReadOnlyField(source="categoria.nombre")
    categoria_id = serializers.PrimaryKeyRelatedField(
        source="categoria", queryset=CategoriaVuelo.objects.all(), write_only=True
    )

    class Meta:
        model = Vuelo
        fields = ("id", "nombre", "slug", "precio", "asientos_disponibles", "esta_activo",
                  "categoria_id", "nombre_categoria", "creado_en", "actualizado_en")
        read_only_fields = ("id", "creado_en", "actualizado_en", "nombre_categoria")
