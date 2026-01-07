from django.urls import path
from .admin_views import CreateUserView,UserListView,RoleListView

urlpatterns = [
    path("users/create/", CreateUserView.as_view()),
    path("users/", UserListView.as_view()),
    path("roles/", RoleListView.as_view()),
]
