from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path(r'c_list/', views.get_all_Compradores, name='get_all_compradores'),
    path(r'c_see/<int:pk>/', views.get_Comprador, name='get_comprador'),
    path(r'c_delete/<int:pk>/', views.delete_Comprador, name='delete_comprador'),
    path(r'c_create/', csrf_exempt(views.create_Coprador), name='create_coprador'),

    path(r'e_list/', views.get_all_Empleados, name='get_all_empleados'),
    path(r'e_see/<int:pk>/', views.get_Empleado, name='get_empleado'),
    path(r'e_delete/<int:pk>/', views.delete_Empleado, name='delete_empleado'),
    path(r'e_create/', csrf_exempt(views.create_Empleado), name='create_empleado')
    
]