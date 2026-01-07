from django.core.management.base import BaseCommand
from access.models import Permission

PERMISSIONS = [
    ("admin.user.create", "Create users"),
    ("admin.user.assign_role", "Assign role to user"),
    ("admin.role.create", "Create roles"),
    ("admin.role.assign_permission", "Assign permissions to role"),
    ("admin.team.assign", "Assign user to team"),
    ("audit.view", "View audit logs"),
]

class Command(BaseCommand):
    help = "Seed initial permissions"

    def handle(self, *args, **kwargs):
        for code, desc in PERMISSIONS:
            Permission.objects.get_or_create(
                code=code,
                defaults={"description": desc}
            )

        self.stdout.write(self.style.SUCCESS("Permissions seeded successfully"))
