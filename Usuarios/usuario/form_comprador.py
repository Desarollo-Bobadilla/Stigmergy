from django import forms
from .models import Comprador

class CompradorForm (forms.ModelForm):

    class Meta:

        model = Comprador
        fields = ['id', 'nombre', 'contrasena', 'preferencias', 'direccion']
        labels = {'id': 'ID del Comprador', 'nombre': 'Nombre Completo', 'contrasena': 'Contraseña', 
                    'preferencias': 'Escriba sus preferencias', 'direccion': 'Ingrese la Dirección de su Casa'}