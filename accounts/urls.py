from django.urls import path
from .admin_views import UserListView

urlpatterns = [
    path("users/", UserListView.as_view()),
    
]
