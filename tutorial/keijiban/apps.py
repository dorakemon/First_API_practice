from django.apps import AppConfig


class KeijibanConfig(AppConfig):
    name = 'keijiban'

    def ready(self):
        import keijiban.signals
