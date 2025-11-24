from rest_framework import viewsets, filters
from catalog.models import Vuelo
from catalog.serializers import VueloSerializer
from catalog.permissions import IsAdminOrReadOnly
from catalog.pagination import StandardResultsSetPagination

class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.select_related("categoria").all()
    serializer_class = VueloSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre", "slug", "categoria__nombre")
    ordering_fields = ("precio", "creado_en", "nombre")

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.request.query_params.get("categoria")
        esta_activo = self.request.query_params.get("esta_activo")
        if categoria:
            qs = qs.filter(categoria__id=categoria)
        if esta_activo is not None:
            qs = qs.filter(esta_activo=esta_activo.lower() in ("1", "true", "t", "yes"))
        return qs
