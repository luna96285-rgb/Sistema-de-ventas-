from django.urls import path
from .import views

urlpatterns = [
    path('Registro-usuarios/', views.registroUsuario, name="registro-usuarios"),
    path('Inicio-sesion/', views.inicioSesion, name="login"),
]
