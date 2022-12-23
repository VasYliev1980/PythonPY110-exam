from faker import Faker
import conf
import random
import datetime
import linecache
import json

fake = Faker(locale="ru_RU")

def check_field_length(field_name: str, max_length: int):
    def decorator(f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs):
            if len(res) > max_length