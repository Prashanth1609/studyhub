from django import template

register = template.Library()

@register.filter
def is_member(session, user):
    """Check if a user is a member of a session."""
    return session.memberships.filter(user=user).exists()

@register.filter
def is_admin(user):
    try:
        return bool(getattr(user, 'is_staff', False) or getattr(user, 'is_superuser', False))
    except Exception:
        return False

@register.filter
def is_leader(user):
    try:
        profile = getattr(user, 'profile', None)
        return bool(profile and getattr(profile, 'is_student_leader', False))
    except Exception:
        return False
