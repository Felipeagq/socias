from rest_framework.serializers import ModelSerializer
from usuarios.models import UsuarioSociasModel

class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = UsuarioSociasModel
        fields = "__all__"