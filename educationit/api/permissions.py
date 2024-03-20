from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class OnlyForMe(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user
        return user.id == 1
