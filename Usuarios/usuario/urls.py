from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path(r'c_list/', views.get_all_compradores_v, name='get_all_compradores_v'),
    path(r'c_see/<int:pk>/', views.get_comprador_v, name='get_comprador_v'),
    path(r'c_delete/<int:pk>/', views.delete_comprador_v, name='delete_comprador_v'),
    path(r'c_create/', csrf_exempt(views.create_coprador_v), name='create_coprador_v'),

    path(r'e_list/', views.get_all_empleados_v, name='get_all_empleados_v'),
    path(r'e_see/<int:pk>/', views.get_empleado_v, name='get_empleado_v'),
    path(r'e_delete/<int:pk>/', views.delete_empleado_v, name='delete_empleado_v'),
    path(r'e_create/', csrf_exempt(views.create_empleado_v), name='create_empleado_v')
    
]