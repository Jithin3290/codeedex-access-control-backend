from django.urls import path
from .admin_views import AssignRoleToUserView

urlpatterns = [
    path("users/assign-role/", AssignRoleToUserView.as_view()),
]
