from teams.models import TeamMembership
from core.permissions import get_user_permissions


def filter_queryset_by_scope(user, queryset, permission_code):
    # Superuser sees everything
    if user.is_superuser:
        return queryset

    perms = get_user_permissions(user)
    scopes = {scope for code, scope in perms if code == permission_code}

    if not scopes:
        return queryset.none()

    if "global" in scopes:
        return queryset

    if "team" in scopes:
        memberships = TeamMembership.objects.filter(user=user)
        if not memberships.exists():
            return queryset.none()

        teams = memberships.values_list("team", flat=True)
        return queryset.filter(teammembership__team__in=teams)

    if "self" in scopes:
        return queryset.filter(id=user.id)

    return queryset.none()
