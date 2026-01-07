from rest_framework.permissions import BasePermission
from access.models import Permission

from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions  # adjust import

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required = getattr(view, "required_permission", None)
        if not required:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        user_perms = get_user_permissions(user)
        user_perm_codes = {code for code, scope in user_perms}

        return required in user_perm_codes
