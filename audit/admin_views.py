from rest_framework.views import APIView
from rest_framework.response import Response

from core.admin_permissions import IsAdminWithPermission
from audit.models import AuditLog

from django.contrib.auth import get_user_model
from access.models import Role

User = get_user_model()

class AuditLogListView(APIView):
    permission_classes = [IsAdminWithPermission]
    required_permission = "audit.view"

    def get(self, request):
        logs = AuditLog.objects.all()[:100]
        data = []

        for log in logs:
            target = log.target
            resolved_target = target

            # Handle ASSIGN_ROLE case
            if log.action == "ASSIGN_ROLE":
                try:
                    parts = dict(p.split(":") for p in target.split(","))
                    user = User.objects.get(id=parts["user"])
                    role = Role.objects.get(id=parts["role"])
                    resolved_target = f"user:{user.username}, role:{role.name}"
                except Exception:
                    pass  # fallback to raw target

            # Handle CREATE_USER
            if log.action == "CREATE_USER":
                try:
                    _, user_id = target.split(":")
                    user = User.objects.get(id=user_id)
                    resolved_target = f"user:{user.username}"
                except Exception:
                    pass

            data.append({
                "actor": log.actor.username if log.actor else None,
                "action": log.action,
                "target": resolved_target,
                "created_at": log.created_at,
            })

        return Response(data)
