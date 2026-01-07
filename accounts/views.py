from rest_framework.views import APIView
from rest_framework.response import Response
from core.drf_permissions import HasPermission
from django.contrib.auth import get_user_model

from core.scope import filter_queryset_by_scope
class MeView(APIView):
    permission_classes = [HasPermission]
    required_permission = "user.view"

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username
        })


User = get_user_model()

class UserListView(APIView):
    permission_classes = [HasPermission]
    required_permission = "user.view"

    def get(self, request):
        qs = User.objects.all()
        qs = filter_queryset_by_scope(
            request.user,
            qs,
            "user.view"
        )

        data = [
            {"id": u.id, "username": u.username}
            for u in qs
        ]

        return Response(data)
