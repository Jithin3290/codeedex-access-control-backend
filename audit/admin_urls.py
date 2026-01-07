from django.urls import path
from .admin_views import AuditLogListView

urlpatterns = [
    path("audit/", AuditLogListView.as_view()),
]
