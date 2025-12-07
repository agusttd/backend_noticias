from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, CategoriaViewSet, ComentarioViewSet, RegistroUsuarioView, LogoutView

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistroUsuarioView.as_view(), name='registro'), 
    path('logout/', LogoutView.as_view(), name='logout'), 
]