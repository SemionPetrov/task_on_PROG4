from extensions import db
from datetime import datetime
import requests
from xml.etree import ElementTree


class CurrencyRates(db.Model):
    __tablename__ = 'currency_rates'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True)
    rate = db.Column(db.Float)
    name = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class CurrencyModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tracked_currencies = ['USD', 'EUR']
        return cls._instance

    def fetch_rates(self):
        try:
            response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
            response.raise_for_status()
            tree = ElementTree.fromstring(response.content)

            rates = {}
            for code in self.tracked_currencies:
                element = tree.find(f".//Valute[CharCode='{code}']")
                if element is not None:
                    value = float(element.find('Value').text.replace(',', '.'))
                    name = element.find('Name').text
                    rates[code] = {'rate': value, 'name': name}
            return rates
        except Exception as e:
            print(f"Ошибка получения курсов: {e}")
            return {}