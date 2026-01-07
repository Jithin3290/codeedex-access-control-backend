from django.utils.timezone import now

def is_active(starts_at, ends_at):
    if starts_at and starts_at > now():
        return False
    if ends_at and ends_at < now():
        return False
    return True

def get_user_permissions(user):
    perms = []

    # Role-based permissions (GLOBAL by default)
    for ur in user.userrole_set.select_related("role"):
        if is_active(ur.starts_at, ur.ends_at):
            for p in ur.role.permissions.all():
                perms.append((p.code, "global"))

    # Direct user permissions (scoped)
    for up in user.userpermission_set.select_related("permission"):
        if is_active(up.starts_at, up.ends_at):
            perms.append((up.permission.code, up.scope))

    return perms

