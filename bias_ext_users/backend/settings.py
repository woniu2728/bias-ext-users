from __future__ import annotations

from bias_core.extensions import SettingsExtender

from bias_ext_users.backend.mail_templates import mail_setting_defaults


def build_mail_settings_extender():
    extender = SettingsExtender(generated_page=False)
    for key, value in mail_setting_defaults().items():
        extender = extender.default(f"mail.{key}", value)
    return extender
