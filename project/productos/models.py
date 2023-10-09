from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    valor = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.nombre