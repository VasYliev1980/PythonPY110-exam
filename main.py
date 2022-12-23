from faker import Faker
import conf
import random
import datetime
import linecache
import json

fake = Faker(locale="ru_RU")

def check_field_length(field_name: str, max_length: int):   # Фабрика декораторов, проверяющая ограничение длинны max_lengthсимволов для поля field_name
    def decorator(f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs):
            if len(res) > max_length:
                raise ValueError(f"Длинна поля {field_name} ghtdsiftn {max_length} символов")
            return res
        return wrapper
    return decorator


@check_field_length("title", 25)   # С помощью фабрики декоратора задаем ограничение длинны в 25 символов для поля title
def get_title() -> str: # Функция получения поля title
    return linecache.getline("books.txt", random.randint(1, 5)).strip()



