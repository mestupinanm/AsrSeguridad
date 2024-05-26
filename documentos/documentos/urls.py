from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url('^documentos/', views.DocumentList),
    path('documentupload/', csrf_exempt(views.documentUpload), name='documentUpload'),
    url('docu2/', views.tipoListV2, name='tipoList'),
]