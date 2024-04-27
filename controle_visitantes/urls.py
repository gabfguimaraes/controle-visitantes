from django.contrib import admin
from django.urls import path

from dashboard.views import index
import visitantes.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "", 
        index, 
        name="index"
        ),
    
    path(
        "registrar-visitante/",
        visitantes.views.registrar_visitante,
        name="registrar_visitante",
    ),
    
    path(
        "visitantes/<int:id>/",
        visitantes.views.informacoes_visitante,
        name="informacoes_visitante",
    ),
    path(
        "visitantes/<int:id>/finalizar-visita/",
        visitantes.views.finalizar_visita,
        name="finalizar_visita"
    )
]
