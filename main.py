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


def get_year() -> int: # Функция получения поля Year
    return random.randint(1900, datetime.datetime.now().year)

def get_pages() -> int: # функция получения поля pages
    return random.randint(0,10000)

def get_isbn13() -> str:  # Функция получения поля isbn13
    return fake.isbn13()

def get_raiting() -> float: # Функция получения поля raiting
    return random.uniform(0, 5)

def get_price() -> float: # Функция получения поля price
    return random.uniform(0, 10000)

def get_authors() -> list[str]: # Функция получения поля authors
    return list(fake.name() for _ in range(random.randint(1, 3)))

def gen_dir(num:int = 1) -> dir: # Функция-генератор словарей
    pk = num
    while True:
        yield {
            "model": conf.MODEL,
            "pk":pk,
            "fields":{
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "raiting": get_raiting(),
                "price": get_price(),
                "authors": get_authors()
            }
        }
        pk += 1

def main() -> None:
    file_name = "dir.json"

    # Генерация и запись словарей в файл
    gen = gen_dir(5)
    with open(file_name, "w") as fout:
        fout.write(json.dumps(list(next(gen) for _ in range(100)), indent=4, ensure_ascii=False))


    # Проверка записанных в файл словарей
    with open(file_name) as fin:
        for s in fin:
            print(s, end="")


if __name__ == "__main__":
    main()