from datetime import datetime, timezone
from flask import render_template

class CurrencyView:
    @staticmethod
    def render_rates(rates):
        return render_template(
            'currency.html',
            rates=rates,
            last_updated=datetime.now(timezone.utc)
        )