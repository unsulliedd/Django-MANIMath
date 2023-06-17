from django.apps import AppConfig

class MANIMath_AccountConfig(AppConfig):
    name = 'MANIMath_Account'
    
    def ready(self):
        import MANIMath_Account.signals