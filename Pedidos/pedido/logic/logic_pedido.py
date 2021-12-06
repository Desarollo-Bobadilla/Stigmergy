from ..models import Pedido

def get_ordenes():
    return Pedido.objects.all().order_by('pk')[:10]

def create_orden(form):
    orden = form.save()
    orden.save()
    return ()

def get_orden_pk(n):
    return Pedido.objects.get(pk = n)

def delete_orden_pk(n):
    Pedido.objects.filter(pk = n).delete()

def change_value_orden_pk(n):
    orden = Pedido.objects.get(pk = n)
    orden.status = 'Alistamiento'
    orden.save()