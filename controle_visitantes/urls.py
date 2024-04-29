from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index
import visitantes.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),
    
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),

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
