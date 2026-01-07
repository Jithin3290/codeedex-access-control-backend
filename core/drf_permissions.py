from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions

class HasPermission(BasePermission):
    required_permission = None

    def has_permission(self, request, view):
        if not self.required_permission:
            return True

        perms = get_user_permissions(request.user)
        return any(p[0] == self.required_permission for p in perms)
