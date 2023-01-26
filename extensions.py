import requests
import json
from config import keys

class ConversionExeption(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionExeption ( f'Невозможно перевести одинаковые валюты {base}.')
        try :
            quote_ticker = keys[quote]
        except KeyError :
            raise ConversionExeption ( f'Не удалось обработать валюту {quote}.' )

        try :
            base_ticker = keys[base]
        except KeyError :
            raise ConversionExeption ( f'Не удалось обработать валюту {base}.' )

        try:
            amount = float(amount)
        except ValueError :
            raise ConversionExeption ( f'Не удалось обработать количество {amount}.' )

        r = requests.get(f'https://v6.exchangerate-api.com/v6/d7cce470da56ef226d8263fd/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate'] * float(amount)
        return total_base
