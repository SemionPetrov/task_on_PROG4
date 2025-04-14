from flask import Flask
from extensions import db
from controllers.currency import currency_blueprint
import os

def create_app():
    app = Flask(__name__)

    # Настройка базы данных
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'currency.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений
    db.init_app(app)

    # Регистрация блюпринтов
    app.register_blueprint(currency_blueprint)

    # Создание таблиц БД
    with app.app_context():
        if not os.path.exists(os.path.join(BASE_DIR, 'instance')):
            os.makedirs(os.path.join(BASE_DIR, 'instance'))
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)