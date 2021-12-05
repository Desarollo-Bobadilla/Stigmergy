from django import forms
from .models import Empleado

class EmpleadoForm (forms.ModelForm):

    class Meta:

        model = Empleado
        fields = ['id', 'nombre', 'contrasena', 'cargo']
        labels = {'id': 'ID del Comprador', 'nombre': 'Nombre Completo', 'contrasena': 'Contraseña', 'cargo': 'Ingrese su Cargo Actual'}