from .models import Document
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json


def check_tipo(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    tipos = r.json()
    for tipo in tipos:
        if data["tipo"] == tipo["id"]:
            return True
    return False

def DocumentList(request):
    
    queryset = Document.objects.all()
    context = list(queryset.values('id', 'variable', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)
    
    

def DocumentCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_tipo(data_json) == True:
            document = Document()
            document.variable = data_json['variable']
            document.value = data_json['value']
            document.unit = data_json['unit']
            document.place = data_json['place']
            document.save()
            return HttpResponse("successfully created document")
        else:
            return HttpResponse("unsuccessfully created document. Variable does not exist")

def DocumentsCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        document_list = []
        for document in data_json:
                    if check_tipo(document) == True:
                        db_document = Document()
                        db_document.variable = document['variable']
                        db_document.value = document['value']
                        db_document.unit = document['unit']
                        db_document.place = document['place']
                        document_list.append(db_document)
                    else:
                        return HttpResponse("unsuccessfully created measurement. Variable does not exist")
        
        Document.objects.bulk_create(document_list)
        return HttpResponse("successfully created document")