
from django.conf.urls import url

from .views import comercio, average, comercio_detail

urlpatterns =[
    url(r'^comercio/$', comercio),
    url(r'^comercio/(?P<pk>\w+)/$', comercio_detail),
    url(r'^average/(?P<pk>\w+)/$', average)
]