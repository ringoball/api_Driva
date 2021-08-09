import swapi
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello(request):
    return HttpResponse("World")

@csrf_exempt
def soma(request):
    json_data = json.loads(request.body.decode(encoding='UTF-8'))
    numero1 = json_data['numero1']
    numero2 = json_data['numero2']
    resultado = numero1 + numero2
    return HttpResponse(resultado)


def starwars(request):
    imprimir = []
    request = requests.get('https://swapi.dev/api/films/')
    lista_filmes = json.loads(request.content)
    for nomes_filmes in lista_filmes['results']:
       imprimir.append(nomes_filmes['title'] + '\n ')
    return HttpResponse(imprimir)
    