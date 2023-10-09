from django import forms 

from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.productos
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]