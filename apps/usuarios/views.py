from django.shortcuts import render
# from django.http import HttpResponse
from visitantes.models import Visitante

def index(request):
#    return HttpResponse("Olá Mundo!")
    todos_visitantes = Visitante.objects.all()
    
    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
    }
    
    return render(request, "index.html", context)
