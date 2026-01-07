from rest_framework.permissions import BasePermission
from access.models import Permission

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required = getattr(view, "required_permission", None)
        if not required:
            return True

        user = request.user

        if not user or not user.is_authenticated:
            return False

        # admins do not bypass permissions
        if not getattr(user, "is_admin", False):
            return False

        # permission must exist in DB
        return Permission.objects.filter(code=required).exists()
