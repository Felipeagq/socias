# Create your views here.
from proyectos_socias.models import Proyectos, Publicaciones
from proyectos_socias.serializers import ProyectosSerializers, PublicacionesSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello_check(request):
    return Response({
        "msg":"ok",
        "status":200,
        "data":{
            "titulo":"backend_Proyecto_socias",
            "version":"v0.0.1"
        }
    })


@api_view(["GET"])
def proyecto_general_api_view(request):
    proyectos = Proyectos.objects.all()
    proyectos_serializer = ProyectosSerializers(
        proyectos,
        many=True
    )
    return Response(
        data = {
            "msg":"proyectos",
            "data": proyectos_serializer.data
        },
        status=200
    )


@api_view(["GET"])
def proyecto_detalle_api_view(request,pk):
    proyectos = None
    # query = Proyectos.objects.get(pk=pk)
    # proyectos = Proyectos.objects.filter(Titulo=query).first()
    proyectos = Proyectos.objects.get(pk=pk)
    print("aqui")
    print(f"-------{proyectos}")
    proyectos_serializer = ProyectosSerializers(
        proyectos,
        many=False
    )
    if proyectos_serializer.data:
        return Response(
            data = {
                "msg":"proyectos",
                "data": proyectos_serializer.data
            },
            status=200
        )
    return Response(
        data = {
            "msg":"No se encontró",
            "data": proyectos_serializer.error
        },
        status=200
    )



@api_view(["GET"])
def publicacione_general_api_view(request):
    publicaciones = Publicaciones.objects.all()
    publicaciones_serializer = PublicacionesSerializers(
        publicaciones,
        many=True
    )
    return Response(
        data = {
            "msg":"Publicaciones",
            "data": publicaciones_serializer.data
        },
        status=200
    )


@api_view(["GET"])
def publicacione_detalle_api_view(request,pk):
    # query = Publicaciones.objects.get(pk=pk)
    # Publicaciones = Publicaciones.objects.filter(Titulo=query).first()
    publicaciones = Publicaciones.objects.get(pk=pk)
    publicaciones_serializer = PublicacionesSerializers(
        publicaciones,
        many=False
    )
    return Response(
        data = {
            "msg":"Publicaciones",
            "data": publicaciones_serializer.data
        },
        status=200
    )
