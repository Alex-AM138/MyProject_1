def filter_by_currency(transactions: list, currency: str) -> list:
        result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
        yield result


def transaction_descriptions( transactions: list) -> str:
    result = map(lambda x: x["description"], transactions)
    for i in result:
        yield i


def card_number_generator(start: int, stop: int) -> str:
    card_number = ""
    for i in range(start, stop):
        card_number = "0" * (16 - len(str(i))) + str(i)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
