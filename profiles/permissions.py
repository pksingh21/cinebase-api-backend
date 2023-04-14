from rest_framework import permissions

from profiles.models import Role


class IsDataEntryist(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        user_roles = Role.objects.filter(user=request.user)
        try:
            user_roles.get(role=Role.ADMIN)
            return True
        except Role.DoesNotExist:
            try:
                user_roles.get(role=Role.DATA_ENTRY)
                return True
            except Role.DoesNotExist:
                return False

    def has_object_permission(self, request, view, obj):
        return True


class IsDataEntryistOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False

        user_roles = Role.objects.filter(user=request.user)
        try:
            user_roles.get(role=Role.ADMIN)
            return True
        except Role.DoesNotExist:
            try:
                user_roles.get(role=Role.DATA_ENTRY)
                return True
            except Role.DoesNotExist:
                return False

    def has_object_permission(self, request, view, obj):
        return True
