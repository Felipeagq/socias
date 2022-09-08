from django.contrib import admin
from proyectos_socias.models import Proyectos, Publicaciones, Etiquetas, Categorias

# Register your models here.
admin.site.register(Proyectos)
admin.site.register(Publicaciones)
admin.site.register(Etiquetas)
admin.site.register(Categorias)
