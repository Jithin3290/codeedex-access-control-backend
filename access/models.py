from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
class UserPermission(models.Model):
    SCOPE_CHOICES = [
        ("self", "Self"),
        ("team", "Team"),
        ("global", "Global"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    scope = models.CharField(max_length=10, choices=SCOPE_CHOICES)
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

