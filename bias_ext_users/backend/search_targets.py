from __future__ import annotations


def user_search_target_provider() -> dict:
    from bias_ext_users.backend.models import User

    return {
        "model": User,
    }

