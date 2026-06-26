import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test-secret-key-for-bias-ext-users"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bias_core",
    "bias_ext_approval.backend.apps.ApprovalExtensionConfig",
    "bias_ext_discussions.backend.apps.DiscussionsExtensionConfig",
    "bias_ext_emoji.backend.apps.EmojiExtensionConfig",
    "bias_ext_flags.backend.apps.FlagsExtensionConfig",
    "bias_ext_likes.backend.apps.LikesExtensionConfig",
    "bias_ext_mentions.backend.apps.MentionsExtensionConfig",
    "bias_ext_notifications.backend.apps.NotificationsExtensionConfig",
    "bias_ext_points.backend.apps.PointsExtensionConfig",
    "bias_ext_posts.backend.apps.PostsExtensionConfig",
    "bias_ext_realtime.backend.apps.RealtimeExtensionConfig",
    "bias_ext_search.backend.apps.SearchExtensionConfig",
    "bias_ext_security.backend.apps.SecurityExtensionConfig",
    "bias_ext_subscriptions.backend.apps.SubscriptionsExtensionConfig",
    "bias_ext_tags.backend.apps.TagsExtensionConfig",
    "bias_ext_uploads.backend.apps.UploadsExtensionConfig",
    "bias_ext_users.backend.apps.UsersExtensionConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "bias_core.middleware.ExtensionErrorHandlingMiddleware",
    "bias_core.middleware.ExtensionRuntimeInvalidationMiddleware",
    "bias_core.middleware.ExtensionCsrfMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "bias_core.middleware.ExtensionThrottleApiMiddleware",
    "bias_core.middleware.ExtensionRequestMiddleware",
    "bias_core.middleware.SecurityHeadersMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "tests.urls"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "test_bias_ext_users.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATIC_URL = "/static/"
FRONTEND_URL = "http://localhost:5173"
DEFAULT_FROM_EMAIL = "Bias <noreply@example.com>"
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
EMAIL_HOST = ""
EMAIL_PORT = 587
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = "test-mail-password"
EMAIL_HOST_USER = "noreply@example.com"
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = "users.User"

NINJA_JWT = {
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "test-jwt-secret-key",
    "ACCESS_TOKEN_LIFETIME": 900,
    "REFRESH_TOKEN_LIFETIME": 86400,
}

from types import SimpleNamespace
BOOTSTRAP = SimpleNamespace(installed=True, debug=True)
