import json
from typing import Any

import src.decorators as decorators
import src.external_api as api


@decorators.log(filename="log.txt")  # type: ignore[operator]
def get_json_transactions(filename: str = "") -> Any:
    """
    Функция, принимает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        transactions = json.load(open(filename, encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    else:
        return transactions


@decorators.log(filename="log.txt")  # type: ignore[operator]
def get_transaction_amount(transaction: dict = {}) -> float:
    """
    Функция, принимает на вход транзакцию и возвращает конвертированную сумму транзакции в рублях
    """
    print(transaction)
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        result = api.currency_conversion(transaction)
        return result
