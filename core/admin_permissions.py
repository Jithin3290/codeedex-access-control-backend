from core.drf_permissions import HasPermission


class IsAdminWithPermission(HasPermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Superuser bypass
        if user.is_superuser:
            return True

        # Custom admin flag check
        if not getattr(user, "is_admin", False):
            return False

        return super().has_permission(request, view)
