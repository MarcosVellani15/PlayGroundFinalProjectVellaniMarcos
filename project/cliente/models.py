from django.db import models

# Create your models here.
class Pais(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name 
    
class clientes(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth = models.DateField(null=True)
    country_origin_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
    
class productos(models.Model):
    pass
