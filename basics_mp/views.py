from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def agregar_vuelo(request):
    try:
        origen = request.data.get('origen', '')
        destino = request.data.get('destino', '')
        fecha = request.data.get('fecha', '')
        precio = float(request.data.get('precio', 0))
        asientos_disponibles = int(request.data.get('asientos_disponibles', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        "origen": origen,
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "asientos_disponibles": asientos_disponibles,
        "mensaje": f"Vuelo de {origen} a {destino} registrado con éxito"
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def actualizar_disponibilidad_vuelo(request):
    try:
        vuelo_id = request.data.get('vuelo_id', '')
        asientos_actuales = int(request.data.get('asientos_actuales', 0))
        asientos_nuevos = int(request.data.get('asientos_nuevos', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    total_asientos = asientos_actuales + asientos_nuevos
    return Response({
        "vuelo_id": vuelo_id,
        "asientos_actuales": asientos_actuales,
        "asientos_nuevos": asientos_nuevos,
        "total_asientos": total_asientos
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def calcular_total_reservas(request):
    try:
        reservas = request.data.get('reservas', [])
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    total_reservas = 0
    for reserva in reservas:
        try:
            total_reservas += float(reserva.get('precio', 0)) * int(reserva.get('cantidad', 0))
        except (TypeError, ValueError):
            return Response({"error": f"Valores invalidos para reserva de vuelo {reserva.get('vuelo_id', '')}"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        "reservas": reservas,
        "total_reservas": total_reservas
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def vuelos_por_disponibilidad_minima(request):
    try:
        vuelos = request.data.get('vuelos', [])
        minimo = int(request.data.get('minimo', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    vuelos_filtrados = [v for v in vuelos if int(v.get('asientos_disponibles', 0)) < minimo]
    return Response({
        "minimo": minimo,
        "vuelos_baja_disponibilidad": vuelos_filtrados
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def promedio_precio_vuelos(request):
    try:
        vuelos = request.data.get('vuelos', [])
        precios = [float(v.get('precio', 0)) for v in vuelos]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(precios) == 0:
        promedio = 0
    else:
        promedio = sum(precios) / len(precios)
    
    return Response({
        "vuelos": vuelos,
        "promedio_precio": promedio
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def valor_vuelo_con_aumento(request):
    try:
        vuelo_id = request.data.get('vuelo_id', '')
        precio = float(request.data.get('precio', 0))
        porcentaje = float(request.data.get('porcentaje', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    nuevo_precio = precio + (precio * porcentaje / 100)
    return Response({
        "vuelo_id": vuelo_id,
        "precio_original": precio,
        "porcentaje_aumento": porcentaje,
        "nuevo_precio": nuevo_precio
    })
