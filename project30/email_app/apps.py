from django.apps import AppConfig


class EmailAppConfig(AppConfig):
    name = 'email_app'
    def ready(self):
        import email_app.signals    
