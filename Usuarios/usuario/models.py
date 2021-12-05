from django.db import models

class Usuario (models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Comprador (Usuario):

    preferencias = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class Empleado (Usuario):

    cargo = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)