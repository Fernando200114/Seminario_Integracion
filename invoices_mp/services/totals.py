from decimal import Decimal, ROUND_HALF_UP
import os

TASA_IMPUESTO = Decimal(os.getenv('TAX_RATE', '0.12'))

def redondear(cantidad):
    return cantidad.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calcular_detalle(detalle):
    subtotal = Decimal(detalle.precio_unitario) * detalle.cantidad
    impuesto = redondear(subtotal * TASA_IMPUESTO)
    total = redondear(subtotal + impuesto)
    return redondear(subtotal), impuesto, total

def recalcular_factura(factura):
    from invoices.models import DetalleFactura
    detalles = DetalleFactura.objects.filter(factura=factura)
    
    subtotal = sum((d.subtotal_linea for d in detalles), Decimal('0'))
    impuesto = sum((d.impuesto_linea for d in detalles), Decimal('0'))
    total = sum((d.total_linea for d in detalles), Decimal('0'))
    
    factura.subtotal = redondear(Decimal(subtotal))
    factura.impuesto = redondear(Decimal(impuesto))
    factura.total = redondear(Decimal(total))
    factura.save(update_fields=['subtotal', 'impuesto', 'total'])
