from main import CurrencyRates
from controllers.databasecontroller import CurrencyRatesCRUD
from controllers.viewcontroller import ViewController

if __name__ == "__main__":
    c_r = CurrencyRates(['USD', 'EUR'])
    c_r_controller = CurrencyRatesCRUD(c_r)

    # Сохраняем данные в БД
    c_r_controller._create()

    # Читаем данные из БД
    print(c_r_controller._read())

    # Отображаем данные
    view = ViewController(c_r)
    print(view())