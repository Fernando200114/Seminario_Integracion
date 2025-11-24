from django.db import models
from .category import CategoriaVuelo

class Vuelo(models.Model):
    categoria = models.ForeignKey(CategoriaVuelo, on_delete=models.CASCADE, related_name="vuelos")
    nombre = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    asientos_disponibles = models.PositiveIntegerField(default=0)
    esta_activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("categoria", "nombre")
        ordering = ("-creado_en",)

    def __str__(self):
        return self.nombre
