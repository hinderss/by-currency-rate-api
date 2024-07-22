import datetime
from urllib.parse import urljoin
import requests


class Bank:
    def __init__(self, config):
        self.currencies_url = config['currencies_url']
        self.rates_url_base = config['rates_url_base']
        self.rates_url_parammode = config['rates_url_parammode']
        self.rates_url_ondate = config['rates_url_ondate']

    def get_currencies(self):
        response = requests.get(self.currencies_url)
        now = datetime.datetime.now()
        print(f'[{datetime.datetime.strftime(now, "%d/%b/%Y %H:%M:%S")}] '
              f'BANK {self.currencies_url} {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            currencies = set()
            for i in data:
                currencies.add(i['Cur_Abbreviation'])
            return currencies
        else:
            raise Exception(f"Request failed. Status code: {response.status_code}")

    def get_rate(self, cur_code, date=None):
        if date is not None:
            url = urljoin(self.rates_url_base, f"{cur_code}{self.rates_url_parammode}{self.rates_url_ondate}{date}")
        else:
            url = urljoin(self.rates_url_base, f"{cur_code}{self.rates_url_parammode}")
        response = requests.get(url)
        now = datetime.datetime.now()
        print(f'[{datetime.datetime.strftime(now, "%d/%b/%Y %H:%M:%S")}] BANK {url} {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            return data['Cur_OfficialRate']
        else:
            raise Exception(f"Request failed. Status code: {response.status_code}")
