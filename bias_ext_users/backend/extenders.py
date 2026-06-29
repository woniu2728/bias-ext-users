from __future__ import annotations

from bias_core.extensions import (
    AdminSurfaceExtender,
    ApiResourceExtender,
    ApiRoutesExtender,
    ForumPermissionExtender,
    LifecycleExtender,
    ModelExtender,
    SearchIndexExtender,
    ServiceProviderExtender,
    UserExtender,
)

from bias_ext_users.backend.admin_api import router as admin_users_router
from bias_ext_users.backend.admin_surface import admin_page_definitions, permission_definitions
from bias_ext_users.backend.api import router as users_router
from bias_ext_users.backend.frontend import frontend_extender
from bias_ext_users.backend.handlers import user_resource_endpoints
from bias_ext_users.backend.model_contracts import owned_models
from bias_ext_users.backend.resources import (
    admin_stats_resource_field_definitions,
    user_resource_definitions,
    user_resource_field_definitions,
    user_resource_relationship_definitions,
)
from bias_ext_users.backend.runtime import user_model_provider, user_service_provider
from bias_ext_users.backend.search_contracts import search_index_definitions
from bias_ext_users.backend.search_targets import user_search_target_provider
from bias_ext_users.backend.services import UserService
from bias_ext_users.backend.settings import build_mail_settings_extender


def frontend_extenders():
    return (frontend_extender(),)


def admin_extenders():
    return (
        AdminSurfaceExtender(
            permissions=permission_definitions(),
            admin_pages=admin_page_definitions(),
            permissions_pages=("/admin/extensions/users/permissions",),
        ),
        ApiRoutesExtender(
            mounts=(("/users", users_router), ("/admin", admin_users_router)),
            tags=("Users",),
        ),
    )


def resource_extenders():
    return (
        ApiResourceExtender("user_detail")
        .endpoints_with(*user_resource_endpoints())
        .fields(user_resource_field_definitions)
        .relationships(user_resource_relationship_definitions),
        ApiResourceExtender("admin_stats").fields(admin_stats_resource_field_definitions),
        *(ApiResourceExtender(definition) for definition in user_resource_definitions()),
    )


def model_extenders():
    extender = ModelExtender()
    for model, description in owned_models():
        extender = extender.owns(model, description=description)
    return (
        extender,
        UserExtender().model_provider(
            user_model_provider,
            description="提供 core 运行时需要的用户模型查询、在线用户序列化与管理员账号管理能力。",
        ),
    )


def permission_extenders():
    return (
        ForumPermissionExtender().checker(
            "users.forum-permissions",
            UserService.has_forum_permission,
            description="基于用户组、后台权限与扩展策略判断论坛权限。",
        ),
    )


def settings_extenders():
    return (build_mail_settings_extender(),)


def service_extenders():
    return (
        ServiceProviderExtender(
            key="users.service",
            provider=user_service_provider,
        ),
        ServiceProviderExtender(
            key="search.target.user",
            provider=user_search_target_provider,
        ),
        LifecycleExtender(),
    )


def search_extenders():
    extender = SearchIndexExtender()
    for definition in search_index_definitions():
        extender = extender.postgres_index(
            definition["name"],
            drop=definition["drop"],
            create=definition["create"],
            description=definition["description"],
        )
    return (extender,)
