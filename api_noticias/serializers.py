from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categoria, Articulo, Comentario

# Serializer para ver los datos del Autor (Usuario) de forma segura
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(read_only=True) # Muestra el nombre del usuario, no solo el ID

    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ['autor', 'articulo'] # El sistema los asignará automáticamente

class ArticuloSerializer(serializers.ModelSerializer):
    # Nested Serializer: Muestra los comentarios dentro de la noticia
    comentarios = ComentarioSerializer(many=True, read_only=True)
    # Muestra el nombre del autor en lugar de su ID
    autor = serializers.StringRelatedField(read_only=True)

    class Meta:  
        model = Articulo
        fields = '__all__'

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user