from django.urls import path
from . import views

urlpatterns = [
    path('agregar-vuelo/', views.agregar_vuelo),
    path('actualizar-disponibilidad-vuelo/', views.actualizar_disponibilidad_vuelo),
    path('calcular-total-reservas/', views.calcular_total_reservas),
    path('vuelos-por-disponibilidad-minima/', views.vuelos_por_disponibilidad_minima),
    path('promedio-precio-vuelos/', views.promedio_precio_vuelos),
    path('valor-vuelo-con-aumento/', views.valor_vuelo_con_aumento),
]
