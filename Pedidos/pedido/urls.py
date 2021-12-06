from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path(r'list/', views.get_all_ordenes, name='ordenes_list'),
    path(r'see/<int:pk>/', views.get_orden, name='get_orden_by_pk'),
    path(r'delete/<int:pk>/', views.delete_orden, name='delete_orden_by_pk'),
    path(r'change/<int:pk>/', csrf_exempt(views.change_orden), name='change_ordent_by_pk'),
    path(r'create/', csrf_exempt(views.orden_create), name='Orden_Create')
]