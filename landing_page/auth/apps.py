from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'landing_page.auth'
    label = "landing_page.auth"
    verbose_name = "Auth"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
