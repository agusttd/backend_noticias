from django.db import models
from django.contrib.auth.models import User # Importamos el usuario nativo para manejar Autores

# Modelo para las Categorías (Política, Deportes, Tecnología, etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

# Modelo Principal: La Noticia/Artículo
class Articulo(models.Model):
    titulo = models.CharField(max_length=200) #  Búsqueda por título
    contenido = models.TextField()
    # Relación con Usuario (Autor): Si se borra el usuario, se borran sus noticias
    autor = models.ForeignKey(User, on_delete=models.CASCADE) 
    # Relación con Categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Para filtrar por fecha 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"

# Modelo de Comentarios 
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.articulo.titulo}"