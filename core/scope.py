from teams.models import TeamMembership
from core.permissions import get_user_permissions

def filter_queryset_by_scope(user, queryset, permission_code):
    perms = get_user_permissions(user)

    scopes = {scope for code, scope in perms if code == permission_code}

    if not scopes:
        return queryset.none()

    if "global" in scopes:
        return queryset

    if "team" in scopes:
        try:
            team = user.teammembership.team
            return queryset.filter(teammembership__team=team)
        except TeamMembership.DoesNotExist:
            return queryset.none()

    if "self" in scopes:
        return queryset.filter(id=user.id)

    return queryset.none()
