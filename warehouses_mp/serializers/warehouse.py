from rest_framework import serializers
from ..models import Aeropuerto

class AeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeropuerto
        fields = ['codigo', 'nombre', 'direccion', 'ciudad', 'creado_en', 'actualizado_en']
    
    def validate_codigo(self, value):
        if ' ' in value:
            raise serializers.ValidationError('El código no debe contener espacios')
        return value
