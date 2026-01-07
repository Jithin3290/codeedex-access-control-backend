from core.drf_permissions import HasPermission

class IsAdminWithPermission(HasPermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if not getattr(request.user, "is_admin", False):
            return False

        return super().has_permission(request, view)
