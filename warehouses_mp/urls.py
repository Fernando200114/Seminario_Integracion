from django.urls import path
from . import views

urlpatterns = [
    path('aeropuertos/lista', views.obtener_lista_aeropuertos),
    path('aeropuertos', views.crear_aeropuerto),
    path('aeropuertos/<int:aeropuerto_id>/', views.obtener_aeropuerto_por_id),
    path('aeropuertos/<int:aeropuerto_id>/', views.actualizar_aeropuerto),
    path('aeropuertos/<int:aeropuerto_id>/', views.eliminar_aeropuerto)
]
