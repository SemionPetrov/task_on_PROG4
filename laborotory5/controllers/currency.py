from flask import Blueprint
from models.currency import CurrencyRates, CurrencyModel
from views.currency import CurrencyView
from extensions import db

currency_blueprint = Blueprint('currency', __name__)


@currency_blueprint.route('/')
def show_rates():
    model = CurrencyModel()
    rates = model.fetch_rates()

    # Обновление данных в базе
    for code, data in rates.items():
        currency = CurrencyRates.query.filter_by(code=code).first()
        if currency:
            currency.rate = data['rate']
            currency.name = data['name']
        else:
            currency = CurrencyRates(code=code, rate=data['rate'], name=data['name'])
            db.session.add(currency)
    db.session.commit()

    # Отображение данных через представление
    return CurrencyView.render_rates(rates)