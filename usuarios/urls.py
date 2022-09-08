from django.urls import path 
from usuarios.views import hello_world_check_usuarios, api_usuarios_general,api_usuarios_detalles

urlpatterns = [
    path("usuarios",api_usuarios_general),
    path("usuarios/<pk>",api_usuarios_detalles),
]