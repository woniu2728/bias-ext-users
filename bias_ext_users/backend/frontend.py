from __future__ import annotations

from bias_core.extensions import FrontendExtender


def frontend_extender():
    return (
        FrontendExtender(
            admin_entry="extensions/users/frontend/admin/index.js",
            forum_entry="extensions/users/frontend/forum/index.js",
        )
        .route(
            "/login",
            "login",
            "./AuthRouteView.vue",
            order=20,
        )
        .route(
            "/register",
            "register",
            "./AuthRouteView.vue",
            order=21,
        )
        .route(
            "/forgot-password",
            "forgot-password",
            "./AuthRouteView.vue",
            order=22,
        )
        .route(
            "/verify-email",
            "verify-email",
            "./VerifyEmailView.vue",
            title="验证邮箱",
            description="验证你的账号邮箱地址。",
            order=23,
        )
        .route(
            "/reset-password",
            "reset-password",
            "./ResetPasswordView.vue",
            title="重置密码",
            description="设置新的账号登录密码。",
            order=24,
        )
        .route(
            "/profile",
            "profile",
            "./ProfileView.vue",
            requires_auth=True,
            order=50,
        )
        .route(
            "/u/:id",
            "user-profile",
            "./ProfileView.vue",
            order=51,
        )
    )
