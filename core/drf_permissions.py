from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions


class HasPermission(BasePermission):
    """
    Non-admin permission check.
    Admins are allowed by default.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Admins bypass permission checks
        if getattr(user, "is_admin", False):
            return True

        required = getattr(view, "required_permission", None)
        if not required:
            return True

        user_perms = get_user_permissions(user)
        user_perm_codes = {code for code, scope in user_perms}

        return required in user_perm_codes
