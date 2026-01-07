from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from core.admin_permissions import IsAdminWithPermission
from audit.models import AuditLog
from access.models import Role
User = get_user_model()

class CreateUserView(APIView):
    permission_classes = [IsAdminWithPermission]
    required_permission = "admin.user.create"

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "username and password required"}, status=400)

        user = User.objects.create_user(
            username=username,
            password=password
        )

        AuditLog.objects.create(
            actor=request.user,
            action="CREATE_USER",
            target=f"user:{user.id}"
        )

        return Response({"id": user.id}, status=201)

class RoleListView(APIView):
    permission_classes = [IsAdminWithPermission]
    required_permission = "admin.user.assign_role"

    def get(self, request):
        roles = Role.objects.all()
        return Response([
            {"id": r.id, "name": r.name}
            for r in roles
        ])
class UserListView(APIView):
    permission_classes = [IsAdminWithPermission]
    required_permission = "admin.user.assign_role"

    def get(self, request):
        users = User.objects.all()
        return Response([
            {"id": u.id, "username": u.username}
            for u in users
        ])