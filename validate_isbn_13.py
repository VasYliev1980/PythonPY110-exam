import re

def check_isbn13(isbn: str) -> bool:  # Функция проверки строки на соответствие формату ISBN-13
    pattern = r"97[89][- ]\d{1,5}[- ]\d{1,7}[- ]\d{1,6}[- ][\d,X]$"
    if re.match(pattern, isbn) is not None:
        return True
    return False
