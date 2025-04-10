import sys
import functools
import sqlite3
import json
from datetime import datetime

# Параметризованный декоратор
def trace(func=None, *, handle=sys.stdout):
    # Обработка случая, когда декоратор вызывается без аргументов
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        # Вызываем функцию и получаем результат
        result = func(*args, **kwargs)

        # Формируем данные для лога
        log_entry = {
            "datetime": datetime.now().isoformat(),
            "func_name": func.__name__,
            "params": list(args) + [f"{k}={v}" for k, v in kwargs.items()],
            "result": result,
        }

        # Логирование в зависимости от типа handle
        if isinstance(handle, str) and handle.endswith(".json"):
            # Логирование в JSON-файл
            try:
                with open(handle, "a") as f:
                    json.dump(log_entry, f)
                    f.write("\n")
            except Exception as e:
                print(f"Ошибка записи в JSON-файл: {e}", file=sys.stderr)
        elif isinstance(handle, sqlite3.Connection):
            # Логирование в базу данных SQLite
            try:
                cur = handle.cursor()
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS logtable (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datetime TEXT,
                        func_name TEXT,
                        params TEXT,
                        result TEXT
                    )
                    """
                )
                cur.execute(
                    "INSERT INTO logtable (datetime, func_name, params, result) VALUES (?, ?, ?, ?)",
                    (
                        log_entry["datetime"],
                        log_entry["func_name"],
                        ", ".join(map(str, log_entry["params"])),
                        str(log_entry["result"]),
                    ),
                )
                handle.commit()
            except Exception as e:
                print(f"Ошибка записи в базу данных: {e}", file=sys.stderr)
        else:
            # Логирование в консоль или другой поток
            handle.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        return result

    return inner


# Утилита для просмотра логов из базы данных SQLite
def showlogs(con: sqlite3.Connection):
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM logtable")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Ошибка чтения из базы данных: {e}", file=sys.stderr)


# Примеры использования

@trace(handle=sys.stderr)  # Логирование в stderr
def increm(x):
    """Инкремент"""
    return x + 1


@trace(handle=sys.stdout)  # Логирование в stdout
def decrem(x):
    """Декремент"""
    return x - 1


@trace(handle="logger.json")  # Логирование в JSON-файл
def cube(x):
    return x**3


# Подключение к базе данных SQLite в памяти
handle_for_f4 = sqlite3.connect(":memory:")

@trace(handle=handle_for_f4)  # Логирование в базу данных SQLite
def power_four(x):
    return x**4


# Тестирование
print(increm(5))  # Логируется в stderr
print(decrem(5))  # Логируется в stdout
print(cube(3))    # Логируется в logger.json
print(power_four(2))  # Логируется в SQLite

# Просмотр логов из SQLite
showlogs(handle_for_f4)