from django.apps import AppConfig

class OncoeduConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oncoedu'

    def ready(self):
        import oncoedu.signals
