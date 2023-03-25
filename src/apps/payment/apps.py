from django.apps import AppConfig


# class PaymentConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'payment'
# добавили в дефолтные настройки дополнительно папку для корректной работы
class PaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payment'
