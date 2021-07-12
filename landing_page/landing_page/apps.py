from django.apps import AppConfig


class LandingPageConfig(AppConfig):
    name = 'landing_page.landing_page'
    verbose_name = "LandingPage"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
