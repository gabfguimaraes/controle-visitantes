from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#    return HttpResponse("Olá Mundo!")
     context ={
          "nome_pagina": "Início da Dashboard",
     }

     return render(request, 'index.html', context)
