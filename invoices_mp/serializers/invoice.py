from rest_framework import serializers
from invoices.models import Factura, DetalleFactura
from invoices.serializers.detalle import DetalleFacturaSerializer

class FacturaSerializer(serializers.ModelSerializer):
    detalles = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Factura
        fields = ('id', 'numero', 'nombre_cliente', 'email_cliente', 'estado',
                  'subtotal', 'impuesto', 'total', 'creado_en', 'actualizado_en', 'detalles')
        read_only_fields = ('id', 'numero', 'subtotal', 'impuesto', 'total', 'creado_en', 'actualizado_en', 'detalles')

    def get_detalles(self, obj):
        qs = DetalleFactura.objects.filter(factura=obj).select_related('vuelo')
        return DetalleFacturaSerializer(qs, many=True).data

class FacturaCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('nombre_cliente', 'email_cliente')
