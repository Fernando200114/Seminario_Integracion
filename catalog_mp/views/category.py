from rest_framework import viewsets, filters
from catalog.models import CategoriaVuelo
from catalog.serializers import CategoriaVueloSerializer
from catalog.permissions import IsAdminOrReadOnly

class CategoriaVueloViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVuelo.objects.all()
    serializer_class = CategoriaVueloSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre", "slug")
    ordering_fields = ("nombre", "creado_en")
