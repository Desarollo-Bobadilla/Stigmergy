from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path(r'c_list/', views.get_all_Compradores, name='get_all_Compradores'),
    path(r'c_see/<int:pk>/', views.get_Comprador, name='get_Comprador'),
    path(r'c_delete/<int:pk>/', views.delete_Comprador, name='delete_Comprador'),
    path(r'c_create/', csrf_exempt(views.create_Coprador), name='create_Coprador'),

    path(r'e_list/', views.get_all_Empleados, name='get_all_Empleados'),
    path(r'e_see/<int:pk>/', views.get_Empleado, name='get_Empleado'),
    path(r'e_delete/<int:pk>/', views.delete_Empleado, name='delete_Empleado'),
    path(r'e_create/', csrf_exempt(views.create_Empleado), name='create_Empleado')
    
]