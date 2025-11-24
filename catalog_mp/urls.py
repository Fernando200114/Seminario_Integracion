# catalog/urls.py
from rest_framework.routers import DefaultRouter
from catalog.views.category import CategoriaVueloViewSet
from catalog.views.product import VueloViewSet

router = DefaultRouter()
router.register(r'categorias-vuelo', CategoriaVueloViewSet, basename='categoria-vuelo')
router.register(r'vuelos', VueloViewSet, basename='vuelo')

urlpatterns = router.urls
