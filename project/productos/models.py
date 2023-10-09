from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

        def __str__(self) -> str:
            return self.nombre
        
class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria,null=True, on_delete=models.SET_NULL, blank=True, verbose_name="categoría")
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self) -> str:
        return f"{self.nombre} (${self.precio})"