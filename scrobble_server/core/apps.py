from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "scrobble_server.core"
    verbose_name = "Scrobble Server Core Modules"

    def ready(self):
        import scrobble_server.core.signals  # noqa: F401
