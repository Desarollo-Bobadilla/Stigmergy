from ..models import Empleado

def get_all_empleados():
    return Empleado.objects.all().order_by('pk')[:10]

def get_empleado_pk(n):
    return Empleado.objects.get(pk = n)

def create_empleado(form):
    empleado = form.save()
    empleado.save()
    return ()

def delete_empleado_pk(n):
    Empleado.objects.filter(pk = n).delete()