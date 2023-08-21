from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Доступ закрыт!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Доступ закрыт!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.student:
            return True
        return False
