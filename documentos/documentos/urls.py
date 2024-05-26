from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('documentos/', views.DocumentList, name='documentList'),
    path('documentupload/', csrf_exempt(views.documentUpload), name='documentUpload'),
    path('manejador/', views.manejador, name='manejador'),
]
