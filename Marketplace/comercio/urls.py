
from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^variables/$', variables),
    url(r'^variables/(?P<pk>\w+)/$', variablesDetail),
    url(r'^average/(?P<pk>\w+)/$', average)
]