from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.admin_permissions import IsAdminWithPermission
from access.models import UserRole, Role
from django.contrib.auth import get_user_model
from audit.models import AuditLog

User = get_user_model()

class AssignRoleToUserView(APIView):
    permission_classes = [IsAdminWithPermission]
    required_permission = "admin.user.assign_role"

    def post(self, request):
        user_id = request.data.get("user_id")
        role_id = request.data.get("role_id")
        starts_at = request.data.get("starts_at")
        ends_at = request.data.get("ends_at")

        if not user_id or not role_id:
            return Response(
                {"error": "user_id and role_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(id=user_id)
        role = Role.objects.get(id=role_id)

        UserRole.objects.create(
            user=user,
            role=role,
            starts_at=starts_at,
            ends_at=ends_at
        )

        AuditLog.objects.create(
            actor=request.user,
            action="ASSIGN_ROLE",
            target=f"user:{user.id},role:{role.id}"
        )

        return Response({"status": "role assigned"}, status=201)
