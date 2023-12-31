from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre 
    
class clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    

class compra(models.Model):
    nombre_compra = models.CharField(max_length=100)
    precio = models.FloatField(null=True)
    def __str__(self) -> str:
        return f"{self.nombre_compra} {self.precio}"