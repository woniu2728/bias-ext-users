from __future__ import annotations

from bias_ext_users.backend.models import AccessToken, EmailToken, Group, PasswordToken, Permission, User


def owned_models():
    return (
        (User, "用户账号由 users 扩展拥有。"),
        (Group, "用户组由 users 扩展拥有。"),
        (Permission, "用户组权限由 users 扩展拥有。"),
        (AccessToken, "用户访问令牌由 users 扩展拥有。"),
        (EmailToken, "邮箱验证令牌由 users 扩展拥有。"),
        (PasswordToken, "密码重置令牌由 users 扩展拥有。"),
    )
