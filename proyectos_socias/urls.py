from django.urls import path
from .views import hello_check,proyecto_general_api_view,proyecto_detalle_api_view, publicacione_detalle_api_view,publicacione_general_api_view

urlpatterns = [
    path("",hello_check),
    path("proyectos",proyecto_general_api_view),
    path("proyectos/<pk>",proyecto_detalle_api_view),
    path("publicaciones",publicacione_general_api_view),
    path("publicaciones/<pk>",publicacione_detalle_api_view),
]