from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^documentos/', views.DocumentList),
    url(r'^documentcreate/$', csrf_exempt(views.DocumentCreate), name='documentCreate'),
    url(r'^createdocumentos/$', csrf_exempt(views.DocumentCreate), name='createDocumentos'),
]