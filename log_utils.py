import datetime as dt
from pathlib import Path


def logger(function):
    def logged_function(*args, **kwargs):
        with open('log.txt', 'a') as file:
            current_time = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')  # Текущие дата и время в формате ISO 8601.
            result = function(*args, **kwargs)
            file.write(
                f"{current_time} | INFO | Initialized {function.__name__} with {args}, {kwargs}. Returned {result} \n"
            )
            return result
    return logged_function


def logger_with_path_fabric(path):
    Path(f'{path}').mkdir(parents=True, exist_ok=True)  # Создает необходимые директории при необходимости.

    def logger_with_path(function):
        def logged_function(*args, **kwargs):
            with open(f'{path}/log.txt', 'a') as file:
                current_time = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                result = function(*args, **kwargs)
                file.write(
                    f"{current_time} | INFO | Initialized {function.__name__} with {args}, {kwargs}. Returned {result}"
                )
                # Перенос строки сделан отдельной функцией в первую очередь для удовлетворения стандартов PEP8:
                # длина строки не более чем 120 символов.
                file.write('\n')
                return result

        return logged_function

    return logger_with_path
