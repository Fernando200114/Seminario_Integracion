from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Aeropuerto
from ..serializers import AeropuertoSerializer

@api_view(["GET"])
def obtener_lista_aeropuertos(request):
    qs = Aeropuerto.objects.all()
    q = (request.query_params.get("q") or "").strip()
    if q:
        qs = qs.filter(Q(codigo__icontains=q) |
                       Q(nombre__icontains=q) |
                       Q(ciudad__icontains=q))
    data = AeropuertoSerializer(qs, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(["POST"])
def crear_aeropuerto(request):
    serializer = AeropuertoSerializer(data=request.data)
    if serializer.is_valid():
        aeropuerto = serializer.save()
        return Response(AeropuertoSerializer(aeropuerto).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def obtener_aeropuerto_por_id(request, aeropuerto_id: int):
    try:
        aeropuerto = Aeropuerto.objects.get(pk=aeropuerto_id)
    except Aeropuerto.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(AeropuertoSerializer(aeropuerto).data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def actualizar_aeropuerto(request, aeropuerto_id: int):
    try:
        aeropuerto = Aeropuerto.objects.get(pk=aeropuerto_id)
    except Aeropuerto.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AeropuertoSerializer(aeropuerto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def eliminar_aeropuerto(request, aeropuerto_id: int):
    try:
        aeropuerto = Aeropuerto.objects.get(pk=aeropuerto_id)
    except Aeropuerto.DoesNotExist:
        return Response({'Detalle': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
    aeropuerto.delete()
    return Response({'Detalle': 'Registro eliminado'}, status=status.HTTP_200_OK)
