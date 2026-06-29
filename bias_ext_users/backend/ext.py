from bias_ext_users.backend.extenders import (
    admin_extenders,
    frontend_extenders,
    model_extenders,
    permission_extenders,
    resource_extenders,
    search_extenders,
    service_extenders,
    settings_extenders,
)


def extend():
    return [
        *frontend_extenders(),
        *admin_extenders(),
        *resource_extenders(),
        *model_extenders(),
        *permission_extenders(),
        *settings_extenders(),
        *service_extenders(),
        *search_extenders(),
    ]
