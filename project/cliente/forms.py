from django import forms 

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.clientes
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]