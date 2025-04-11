import requests
from xml.etree import ElementTree

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrencyRates(metaclass=SingletonMeta):
    URL = "https://www.cbr.ru/scripts/XML_daily.asp"

    def __init__(self, char_codes=['USD', 'EUR', 'GBP']):
        self._rates = {}
        self._char_codes = None

        if self._check_char_codes(char_codes):
            self._char_codes = char_codes
            self._fetch_rates()
        else:
            raise ValueError('Some char code is not correct')

    @property
    def rates(self):
        return self._rates

    @property
    def char_codes(self):
        return self._char_codes

    @char_codes.setter
    def char_codes(self, new_char_codes):
        if self._check_char_codes(new_char_codes):
            self._char_codes = new_char_codes
            self._fetch_rates()
        else:
            raise ValueError('Invalid char codes')

    @char_codes.deleter
    def char_codes(self):
        self._char_codes = []
        self._rates = {}

    def _check_char_codes(self, char_codes):
        response = requests.get(self.URL)
        if response.status_code == 200:
            tree = ElementTree.fromstring(response.content)
            available_codes = [code.text for code in tree.findall('.//CharCode')]
            return all(code in available_codes for code in char_codes)
        raise ConnectionError("Не удалось получить данные с сайта ЦБ РФ")

    def _fetch_rates(self):
        response = requests.get(self.URL)
        if response.status_code == 200:
            tree = ElementTree.fromstring(response.content)
            self._rates = {}
            for code in self._char_codes:
                element = tree.find(f".//Valute[CharCode='{code}']/Value")
                if element is not None:
                    self._rates[code] = float(element.text.replace(",", "."))
        else:
            raise ConnectionError("Не удалось получить данные с сайта ЦБ РФ")