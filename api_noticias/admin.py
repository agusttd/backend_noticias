from django.contrib import admin
from .models import Categoria, Articulo, Comentario

# Configuración para ver las Categorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

# Configuración para ver los Artículos con filtros
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'created_at') # Columnas visibles
    list_filter = ('categoria', 'created_at') # Filtros laterales
    search_fields = ('titulo', 'contenido') # Barra de búsqueda

# Configuración para ver los Comentarios
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'articulo', 'created_at')