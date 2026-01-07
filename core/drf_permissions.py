from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required = getattr(view, "required_permission", None)
        if not required:
            return True

        user = request.user

        # collect permissions from roles
        role_perms = Permission.objects.filter(
            roles__users=user,
            code=required
        ).exists()

        return role_perms

