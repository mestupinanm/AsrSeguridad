from .models import Tipo
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def TipoList(request):
    queryset = Tipo.objects.all()
    context = list(queryset.values('id', 'name'))
    return render(request, 'tipos/tipos_list.html', context)

def TipoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        tipo = Tipo()
        tipo.name = data_json["name"]
        tipo.save()
        return HttpResponse("successfully created tipo")