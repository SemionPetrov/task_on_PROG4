from datetime import datetime
import sqlite3

class CurrencyRatesCRUD:
    def __init__(self, currency_rates_obj):
        self.__con = sqlite3.connect('data.sqlite3')
        self.__createtable()
        self.__cursor = self.__con.cursor()
        self.__currency_rates_obj = currency_rates_obj

    def __createtable(self):
        self.__con.execute(
            "CREATE TABLE IF NOT EXISTS currency("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "cur TEXT,"
            "date TEXT,"
            "value FLOAT);"
        )
        self.__con.commit()

    def _create(self):
        params = [
            (code, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), rate)
            for code, rate in self.__currency_rates_obj.rates.items()
        ]
        self.__cursor.executemany(
            "INSERT INTO currency(cur, date, value) VALUES(:cur, :date, :value)",
            [{"cur": cur, "date": date, "value": value} for cur, date, value in params]
        )
        self.__con.commit()

    def _read(self, code=None):
        query = "SELECT * FROM currency"
        if code:
            query += " WHERE cur = :code"
            self.__cursor.execute(query, {"code": code})
        else:
            self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def _update(self, code, new_value):
        self.__cursor.execute(
            "UPDATE currency SET value = :value WHERE cur = :code",
            {"code": code, "value": new_value}
        )
        self.__con.commit()

    def _delete(self, code):
        self.__cursor.execute(
            "DELETE FROM currency WHERE cur = :code",
            {"code": code}
        )
        self.__con.commit()