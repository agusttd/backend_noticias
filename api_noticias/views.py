from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Articulo, Categoria, Comentario
from .serializers import ArticuloSerializer, CategoriaSerializer, ComentarioSerializer, RegistroUsuarioSerializer
from .permissions import IsOwnerOrReadOnly 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # Cualquiera puede ver, pero solo admin crea categorías (opcional)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    # Aquí aplicamos la lógica de seguridad:
    # 1. IsAuthenticatedOrReadOnly: Si no estás logueado, solo puedes leer.
    # 2. IsOwnerOrReadOnly: Si estás logueado, solo puedes editar TU artículo.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Configuración de Filtros y Búsqueda 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'created_at'] # Filtrar por categoría y fecha
    search_fields = ['titulo', 'contenido']        # Búsqueda por título y contenido
    ordering_fields = ['created_at']

    # Método mágico para guardar automáticamente al autor
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Asignamos autor y buscamos el artículo asociado si viene en la URL (opcional)
        serializer.save(autor=self.request.user)

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated] # Solo si estás logueado puedes salir

    def post(self, request):
        # Borramos el token para cerrar sesión
        request.user.auth_token.delete()
        return Response({"mensaje": "Sesión cerrada exitosamente"}, status=status.HTTP_200_OK)