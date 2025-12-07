from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Métodos de lectura (GET, HEAD, OPTIONS) están permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.autor == request.user