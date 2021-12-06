from django.db import models

class Producto (models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(null=True, blank=True, default=None)
    alto = models.FloatField(null=True, blank=True, default=None)
    ancho = models.FloatField(null=True, blank=True, default=None)
    largo = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    cantidadDisponible = models.IntegerField()
    
    # .....
    id_sede = models.IntegerField()
    # .....

    def __str__(self):
        return '%s %s' % (self.nombre, self.precio)

class Item (models.Model):
    
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    produc = models.OneToOneField(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.cantidad)


class Pedido (models.Model):

    id = models.AutoField(primary_key=True)
    identificate = models.IntegerField()
    precioTotal = models.FloatField(null=True, blank=True, default=None)

    CREADA = 'Creada'
    ALISTAMIENTO = 'Alistamiento'
    LISTA = 'Lista'
    EN_HUB_DESPACHO = 'En Hub Despacho'
    VOLANDO = 'Volando'
    EN_HUB_LLEGADA = 'En Hub Llegada'
    LISTA_RECOGER = 'Lista Recoger'
    ENTREGADA = 'Entregada'
    CANCELADA = 'Cancelada'

    CHOICES = (
        (CREADA, 'Creada'),
        (ALISTAMIENTO, 'Alistamiento'),
        (LISTA, 'Lista'),
        (EN_HUB_DESPACHO, 'En Hub Despacho'),
        (VOLANDO, 'Volando'),
        (EN_HUB_LLEGADA, 'En Hub Llegada'),
        (LISTA_RECOGER, 'Lista Recoger'),
        (ENTREGADA, 'Entregada'),
        (CANCELADA, 'Cancelada')
    )

    status = models.CharField(max_length=255, choices=CHOICES, default=CREADA)
    items = models.ManyToManyField(Item)

    # .....
    comprador = models.IntegerField(null=True)
    hubEntrega = models.IntegerField(null=True)
    hubRecepcion = models.IntegerField(null=True)
    # .....
 
    def __str__(self):
        return '%s %s' % (self.identificate, self.precioTotal)