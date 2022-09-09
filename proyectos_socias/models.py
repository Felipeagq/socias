from tabnanny import verbose
from django.db import models
from usuarios.models import UsuarioSociasModel
from datetime import datetime

# Create your models here.

class Etiquetas(models.Model):
    etiqueta = models.CharField(max_length=50)
    # id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.etiqueta

    class Meta:
        verbose_name_plural = "Etiqueta"


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name_plural = "Categorías"


class Proyectos(models.Model):
    nombre = models.CharField(
        max_length=100, 
        help_text="Nombre del emprendimiento"
    )
    nit = models.IntegerField(help_text="NIT de la empresa",null=True,blank=True)
    camara_comercio = models.CharField(
        max_length=100,
        help_text="Registro en camara de comercio",
        null=True,
        blank=True
    )
    rut = models.CharField(
        max_length=100,
        help_text="Numero del Registro Unico Tributario (RUT)",null=True,blank=True
    )
    cedula = models.IntegerField(help_text="Numero de cedula de la empresaria",null=True,blank=True)
    video = models.CharField(
        max_length=200,
        help_text="Link a YouTube con video explicativo de la empresa",null=True,blank=True
    )
    informacion = models.TextField(
        help_text="""- Volumen de ventas </br> - Datos de crecimiento </br> - Volumen de usuarios </br> - Plan de inversión </br> """,null=True,blank=True
    )
    estatutos = models.CharField(
        max_length=200,
        help_text="Montada del archivo a S3, convertir a binario y subir",null=True,blank=True
    )
    descripcion_integrantes = models.TextField(
        help_text="""Descripción de o los integrantes de la empresa o proyecto:
Nombre y apellido, mail, números de identificación, roles y HV
en PDF de los integrantes del equipo.""",null=True,blank=True
    )
    accionistas = models.IntegerField(help_text="Cantidad de accionisttas que tiene el proyecto",default=1)
    producto = models.TextField(null=True,blank=True)
    certificado_existencias = models.CharField(max_length=200,help_text="texto de aiuda modificado",null=True,blank=True)

    imagen = models.CharField(max_length=200,null=True,blank=True)
    ciudad = models.CharField(max_length=100,null=True,blank=True,help_text="ciudad donde está el proyecto")
    monto_total = models.IntegerField(null=True,blank=True,help_text="Monto total que pide para la empresa")
    aportes = models.IntegerField(null=True,blank=True,help_text="la cantidad de aportes que le han hecho a su proyecto")
    icono = models.CharField(max_length=150,null=True,blank=True) # hay que ver
    fecha_creacion_empresa = models.DateField(null=True,blank=True, help_text="Fecha en la que se creó o se fundó la empresa")
    fecha_creacion_socias = models.DateField(null=True,blank=True,default=datetime.now(),help_text="Fecha en la que creó el proyecto en Socias, por defecto")

    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True,blank=True,help_text="Categorias a las cuales se posa el proyecto")
    etiquetas = models.ForeignKey(Etiquetas,on_delete=models.CASCADE,default=1,null=False, blank=True,help_text="etiquetas del proyecto")
    usuarios = models.ForeignKey(UsuarioSociasModel,on_delete=models.CASCADE,null=True,blank=True,help_text="Usuario que creoó el proyecto")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proyectos"




class Publicaciones(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)
    icono = models.CharField(max_length=150)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicaciones"