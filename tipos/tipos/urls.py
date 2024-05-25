from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^tipos/', views.TipoList, name='tipoList'),
    url(r'^tipocreate/$', csrf_exempt(views.TipoCreate), name='tipoCreate'),
]