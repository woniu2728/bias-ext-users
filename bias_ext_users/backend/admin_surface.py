from __future__ import annotations

from bias_core.extensions import AdminPageDefinition, PermissionDefinition

from bias_ext_users.backend.constants import EXTENSION_ID


def permission_definitions():
    return (
        PermissionDefinition(
            code="viewUserList",
            label="查看用户列表",
            section="view",
            section_label="查看权限",
            module_id=EXTENSION_ID,
            icon="fas fa-users",
            description="允许浏览用户列表与公开资料。",
        ),
        PermissionDefinition(
            code="searchUsers",
            label="搜索用户",
            section="view",
            section_label="查看权限",
            module_id=EXTENSION_ID,
            icon="fas fa-search",
            description="允许在论坛搜索中查询用户。",
        ),
        PermissionDefinition(
            code="user.edit",
            label="编辑用户资料",
            section="user",
            section_label="用户管理",
            module_id=EXTENSION_ID,
            icon="fas fa-user-edit",
            description="允许管理员编辑任意用户资料与用户组。",
        ),
        PermissionDefinition(
            code="user.suspend",
            label="封禁用户",
            section="user",
            section_label="用户管理",
            module_id=EXTENSION_ID,
            icon="fas fa-user-slash",
            description="允许暂停用户发言能力。",
        ),
    )


def admin_page_definitions():
    return (
        AdminPageDefinition(
            path="/admin/users",
            label="用户管理",
            icon="fas fa-users",
            module_id=EXTENSION_ID,
            nav_section="core",
            description="查看、编辑、分组与封禁论坛用户。",
        ),
    )
