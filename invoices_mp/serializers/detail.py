from rest_framework import serializers
from invoices.models import DetalleFactura
from catalog.models import Vuelo

class DetalleFacturaSerializer(serializers.ModelSerializer):
    vuelo_id = serializers.PrimaryKeyRelatedField(
        source='vuelo', queryset=Vuelo.objects.all(), write_only=True
    )
    nombre_vuelo = serializers.ReadOnlyField(source='vuelo.nombre')

    class Meta:
        model = DetalleFactura
        fields = ('id', 'factura', 'vuelo_id', 'nombre_vuelo', 'cantidad', 'precio_unitario',
                  'subtotal_linea', 'impuesto_linea', 'total_linea')
        read_only_fields = ('id', 'subtotal_linea', 'impuesto_linea', 'total_linea', 'nombre_vuelo')
