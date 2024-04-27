from django.shortcuts import render
# from django.http import HttpResponse
from visitantes.models import Visitante

def index(request):
#    return HttpResponse("Olá Mundo!")
    todos_visitantes = Visitante.objects.all()
    # filtrando os visitantes por status
    visitantes_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitantes_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )
    
    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
    }
    
    return render(request, "index.html", context)
