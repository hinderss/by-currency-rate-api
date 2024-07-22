from django.apps import AppConfig
from django.core.cache import cache

from currencies.api.currency import Bank
from currencies.settings import BANK


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currencies.api'

    def ready(self):
        bank = Bank(BANK)
        currencies = bank.get_currencies()
        cache.set('currencies', currencies, timeout=None)
        cache.set('bank_instance', bank, timeout=None)
