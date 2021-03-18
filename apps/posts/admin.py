from django.contrib import admin
from .models import Post, Categoria

#Configuracion para la visualizacion de Posts y Categorias en panel de Admin.
admin.site.register(Post)
admin.site.register(Categoria)

