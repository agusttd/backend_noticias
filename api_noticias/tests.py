from django.test import TestCase
from django.contrib.auth.models import User
from .models import Categoria, Articulo

class NoticiaModelTest(TestCase):
    
    def setUp(self):
        # 1. Configuración inicial: Creamos un usuario y una categoría de prueba
        self.usuario = User.objects.create_user(username='testuser', password='123')
        self.categoria = Categoria.objects.create(nombre='Ciencia')

    def test_crear_articulo(self):
        """Prueba que se puede crear un artículo correctamente"""
        articulo = Articulo.objects.create(
            titulo='Descubrimiento en Marte',
            contenido='Han encontrado agua...',
            autor=self.usuario,
            categoria=self.categoria
        )
        # Verificamos que se guardó en la base de datos (debería haber 1)
        self.assertEqual(Articulo.objects.count(), 1)
        # Verificamos que el título es correcto
        self.assertEqual(articulo.titulo, 'Descubrimiento en Marte')

    def test_string_representation(self):
        """Prueba que el __str__ del modelo se ve bonito"""
        articulo = Articulo.objects.create(
            titulo='Noticia Importante',
            contenido='Contenido...',
            autor=self.usuario,
            categoria=self.categoria
        )
        # El __str__ debería ser "Titulo por Usuario" (según definimos en models.py)
        esperado = f"Noticia Importante por testuser"
        self.assertEqual(str(articulo), esperado)