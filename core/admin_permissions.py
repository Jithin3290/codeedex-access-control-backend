from core.drf_permissions import HasPermission


class IsAdminWithPermission(HasPermission):
    """
    Admin-only access.
    Admins are allowed immediately.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return getattr(user, "is_admin", False)
