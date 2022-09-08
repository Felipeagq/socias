from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from usuarios.models import TypeUserModel,UsuarioSociasModel
from usuarios.serializers import UsuariosSerializer

# Create your views here.
@api_view(["GET"])
def hello_world_check_usuarios(request):
    return Response({
        "msg":"ok",
        "status":200,
        "data":{
            "titulo":"backend_Proyecto_socias",
            "version":"v0.0.1"
        }
    })


@api_view(["GET"])
def api_usuarios_general(request):
    usuarios = UsuarioSociasModel.objects.all()
    usuarios_serializer = UsuariosSerializer(
        usuarios,
        many=True
    )
    return Response(
        status=200,
        data={
            "msg":"usuarios",
            "data":usuarios_serializer.data
        }
    )


@api_view(["GET"])
def api_usuarios_detalles(request,pk):
    usuarios = UsuarioSociasModel.objects.filter(id=pk).first() #.values("nombres","apellidos","cargo","foto","tipo_id__tipo")
    print(type(usuarios))
    usuarios_serializer = UsuariosSerializer(
        usuarios,
        many=False
    )
    return Response(
        status=200,
        data={
            "msg":"usuarios",
            "data":usuarios_serializer.data
        }
    )