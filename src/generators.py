from typing import Generator

import src.decorators as decorators


@decorators.log(filename="log.txt")  # type: ignore[operator]
def filter_by_currency(transactions: list, currency: str) -> Generator:
    """
    Функция получает на вход список транзакций и возвращает отфильтрованные значения
    в форме генератора
    """
    if transactions[0].get("currency_code") is None:
        result = list(filter(lambda x: x.get("operationAmount").get("currency").get("code") == currency, transactions))
    else:
        result = list(filter(lambda x: x.get("currency_code") == currency, transactions))
    yield result


@decorators.log(filename="log.txt")  # type: ignore[operator]
def transaction_descriptions(transactions: list) -> Generator:
    """
    Функция получает на вход список транзакций и возвращает описание каждой
    транзакции в форме генератора
    """
    result = map(lambda description: description["description"], transactions)
    for i in result:
        yield i


@decorators.log(filename="log.txt")  # type: ignore[operator]
def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция принимает на вход начальное и конечное значение диапазона,
    и генерирует номера карт в этом диапазоне.
    """
    card_number = ""
    for i in range(start, end):
        card_number = "0" * (16 - len(str(i))) + str(i)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:17]}"
