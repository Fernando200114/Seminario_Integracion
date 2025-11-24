from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied, ValidationError
from invoices.models import DetalleFactura
from invoices.serializers.detalle import DetalleFacturaSerializer
from invoices.services import totals

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleFacturaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = DetalleFactura.objects.select_related('factura', 'vuelo')
        if not self.request.user.is_staff:
            queryset = queryset.filter(factura__usuario=self.request.user)
        return queryset

    def perform_create(self, serializer):
        factura = serializer.validated_data['factura']

        if not self.request.user.is_staff and factura.usuario != self.request.user:
            raise PermissionDenied('No puedes modificar facturas de otros usuarios')

        if factura.estado != factura.BORRADOR:
            raise ValidationError('Solo puedes agregar detalles cuando la factura está en Borrador')

        serializer.save()

        totals.recalcular_factura(factura)
