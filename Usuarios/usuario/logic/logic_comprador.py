from ..models import Comprador

def get_all_compradores():
    return Comprador.objects.all().order_by('pk')[:10]

def get_comprador_pk(n):
    return Comprador.objects.get(pk = n)

def create_comprador(form):
    comprador = form.save()
    comprador.save()
    return ()

def delete_comprador_pk(n):
    Comprador.objects.filter(pk = n).delete()