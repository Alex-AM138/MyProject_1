def filter_by_currency(transactions: list, currency: str) -> iter:
    """
    Функция принимает на вход список словарей, представляющих транзакции
        и возвращает итератор, который поочередно выводит
    транзакции, где валюта операции соответствует заданной
    """
    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    yield result


def transaction_descriptions(transactions: list) -> iter:
    """
    Генератор, который принимает список словарей с транзакциями
     и возвращает описание каждой операции по очереди
    """
    result = map(lambda x: x["description"], transactions)
    for i in result:
        yield i


def card_number_generator(start: int, stop: int) -> iter:
    """
        Генератор, который выводит номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    card_number = ""
    for i in range(start, stop):
        card_number = "0" * (16 - len(str(i))) + str(i)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
