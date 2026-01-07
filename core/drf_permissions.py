from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions


class HasPermission(BasePermission):
    required_permission = None

    def has_permission(self, request, view):
        user = request.user

        # Not logged in
        if not user or not user.is_authenticated:
            return False

        # Django superuser = full access
        if user.is_superuser:
            return True

        # If view does not require a permission, allow
        if not self.required_permission:
            return True

        perms = get_user_permissions(user)
        return any(code == self.required_permission for code, _ in perms)
