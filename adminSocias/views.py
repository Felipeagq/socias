from rest_framework.response import Response
from rest_framework .decorators import api_view

@api_view(["GET"])
def hello_check(request):
    return Response({
        "msg":"ok",
        "status":200,
        "data":{
            "titulo":"backend_Proyecto_socias",
            "version":"v0.0.16",
            "rutas":{
                "root":"https://socias-backend.neero.link",
                "admin":"https://socias-backend.neero.link/admin",
                "proyectos":[
                    "https://socias-backend.neero.link/socias/proyectos",
                    "https://socias-backend.neero.link/socias/proyectos/<id>"
                ],
                "publicaciones":[
                    "https://socias-backend.neero.link/socias/publicaciones",
                    "https://socias-backend.neero.link/socias/publicaciones/<id>"
                ],
                "usuarios":[
                    "https://socias-backend.neero.link/socias/usuarios",
                    "https://socias-backend.neero.link/socias/usuarios/<id>",
                ]
            }
        }
    })