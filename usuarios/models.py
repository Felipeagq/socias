from django.db import models

# Create your models here.
class TypeUserModel(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo}"


class UsuarioSociasModel(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.CharField(max_length=200)
    tipo = models.ForeignKey(TypeUserModel,on_delete=models.CASCADE,default=1,null=False,blank=True)

    def __str__(self):
        return f"{self.nombres}"