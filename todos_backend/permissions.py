from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsRegisteredOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_registred = bool(request.user and request.user.is_staff)
        return is_registred or request.method in SAFE_METHODS