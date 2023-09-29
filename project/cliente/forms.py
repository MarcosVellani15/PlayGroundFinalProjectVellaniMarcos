from django import forms 

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.clientes
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]

class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields = ["nombre"]

class CompraForm(forms.ModelForm):
    class Meta:
        model = models.compra
        fields = ["nombre_compra", "precio"]