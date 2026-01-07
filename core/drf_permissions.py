from rest_framework.permissions import BasePermission
from core.permissions import get_user_permissions
from rest_framework.permissions import BasePermission
from access.models import Permission, Role
from accounts.models import UserPermission

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required = getattr(view, "required_permission", None)
        if not required:
            return True

        user = request.user

        # get roles assigned to user
        role_ids = UserPermission.objects.filter(
            user=user
        ).values_list("role_id", flat=True)

        # check if any of those roles has the permission
        return Permission.objects.filter(
            role_id__in=role_ids,
            code=required
        ).exists()
