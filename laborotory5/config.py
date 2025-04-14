import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///currency.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CBR_API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'