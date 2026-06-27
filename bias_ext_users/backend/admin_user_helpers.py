from typing import Any, Dict

from django.utils import timezone
from django.utils.dateparse import parse_datetime

from bias_core.extensions.forum import get_forum_registry
from bias_ext_users.backend.group_utils import get_primary_group, serialize_group_badge
from bias_ext_users.backend.models import Group, User


BUILTIN_GROUPS = {
    1: "Admin",
    2: "Guest",
    3: "Member",
    4: "Moderator",
}


def serialize_group(group: Group) -> Dict[str, Any]:
    payload = serialize_group_badge(group) or {}
    payload["is_system"] = is_builtin_group(group)
    return payload


def validate_group_payload(payload: Dict[str, Any], group: Group = None):
    name = (payload.get("name") or "").strip()
    if not name:
        raise ValueError("用户组名称不能为空")

    queryset = Group.objects.filter(name=name)
    if group is not None:
        queryset = queryset.exclude(id=group.id)
    if queryset.exists():
        raise ValueError("用户组名称已存在")

    return {
        "name": name,
        "name_singular": name,
        "name_plural": name,
        "color": payload.get("color") or "#4d698e",
        "icon": (payload.get("icon") or "").strip(),
        "is_hidden": bool(payload.get("is_hidden", False)),
    }


def is_builtin_group(group: Group) -> bool:
    return BUILTIN_GROUPS.get(group.id) == group.name


def normalize_permission_code(permission: str):
    return get_forum_registry().normalize_permission_code(permission)


def serialize_admin_user(user: User, include_details: bool = False) -> Dict[str, Any]:
    primary_group = get_primary_group(user)
    payload = {
        "id": user.id,
        "username": user.username,
        "email": getattr(user, "email", ""),
        "display_name": getattr(user, "display_name", "") or getattr(user, "username", ""),
        "avatar_url": getattr(user, "avatar_url", ""),
        "is_email_confirmed": bool(getattr(user, "is_email_confirmed", False)),
        "is_staff": bool(getattr(user, "is_staff", False)),
        "is_suspended": bool(getattr(user, "is_suspended", False)),
        "joined_at": getattr(user, "joined_at", None),
        "last_seen_at": getattr(user, "last_seen_at", None),
        "discussion_count": getattr(user, "discussion_count", 0),
        "comment_count": getattr(user, "comment_count", 0),
        "groups": [serialize_group(group) for group in user.user_groups.all().order_by("name")] if hasattr(user, "user_groups") else [],
        "primary_group": serialize_group(primary_group) if primary_group else None,
    }

    if include_details:
        payload.update({
            "bio": getattr(user, "bio", ""),
            "suspended_until": getattr(user, "suspended_until", None),
            "suspend_reason": getattr(user, "suspend_reason", ""),
            "suspend_message": getattr(user, "suspend_message", ""),
        })

    return payload


def parse_optional_datetime(value):
    if value in (None, "", False):
        return None

    parsed = parse_datetime(str(value))
    if not parsed:
        raise ValueError("封禁截止时间格式无效")

    if timezone.is_naive(parsed):
        parsed = timezone.make_aware(parsed, timezone.get_current_timezone())

    return parsed

