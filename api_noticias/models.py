from django.db import models
from django.contrib.auth.models import User # Se imprta el usuario nativo para manejar Autores
from django.core.exceptions import ValidationError

def validar_titulo_largo(valor):
    if len(valor) < 5:
        raise ValidationError('El título es muy corto. Debe tener al menos 5 letras.')

# Modelo para las Categorías 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Principal: La Noticia/Artículo
class Articulo(models.Model):
    titulo = models.CharField(max_length=200, validators=[validar_titulo_largo]) #  Búsqueda por título
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)   # Relación con Usuario (Autor): Si se borra el usuario, se borran sus noticias
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)    # Relación con Categoría
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
    
