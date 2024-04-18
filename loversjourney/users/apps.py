from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "loversjourney.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import loversjourney.users.signals  # noqa: F401
        except ImportError:
            pass
