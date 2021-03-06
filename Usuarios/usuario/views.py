from django.shortcuts import render

from .logic.logic_comprador import get_all_compradores, get_comprador_pk, create_comprador, delete_comprador_pk
from .logic.logic_empleado import get_all_empleados, get_empleado_pk, create_empleado, delete_empleado_pk

from .form_comprador import CompradorForm
from .form_empleado import EmpleadoForm

from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# -----

def get_all_compradores_v(request):

    if request.method == 'GET':
        context = {'compradores_list': get_all_compradores()}
        return render(request, 'Comprador/compradores.html', context)

def get_all_empleados_v(request):

    if request.method == 'GET':
        context = {'empleados_list': get_all_empleados()}
        return render(request, 'Empleado/empleados.html', context)

# -----

def get_comprador_v(request, pk):

    if request.method == 'GET':
        comprador = serializers.serialize('json', [get_comprador_pk(pk)])
        return HttpResponse(comprador, content_type = 'application/json')

def get_empleado_v(request, pk):

    if request.method == 'GET':
        empleado = serializers.serialize('json', [get_empleado_pk(pk)])
        return HttpResponse(empleado, content_type = 'application/json')

# -----

def delete_comprador_v(request, pk):

    if request.method in ['GET', 'DELETE']:
        delete_comprador_pk(pk)
        context = {'compradores_list': get_all_compradores()}
        return render(request, 'Comprador/compradores.html', context)

def delete_empleado_v(request, pk):

    if request.method in ['GET', 'DELETE']:
        delete_empleado_pk(pk)
        context = {'empleados_list': get_all_empleados()}
        return render(request, 'Empleado/empleados.html', context)

# -----

def create_coprador_v(request):

    if request.method == 'POST':

        form = CompradorForm(request.POST)

        if form.is_valid():
            create_comprador(form)
            messages.add_message(request, messages.SUCCESS, 'Comprador create successful')
            return HttpResponseRedirect(reverse('create_coprador_v'))

        else:
            print('\n', form.errors, '\n')

    else:
        form = CompradorForm()

    context = {'form': form,}
    return render(request, 'Comprador/compradorCreate.html', context)

def create_empleado_v(request):

    if request.method == 'POST':

        form = EmpleadoForm(request.POST)

        if form.is_valid():
            create_empleado(form)
            messages.add_message(request, messages.SUCCESS, 'Empleado create successful')
            return HttpResponseRedirect(reverse('create_empleado_v'))

        else:
            print('\n', form.errors, '\n')

    else:
        form = EmpleadoForm()

    context = {'form': form,}
    return render(request, 'Empleado/empleadoCreate.html', context)