import json
import logging
import os
from typing import Any

import src.external_api as api

ROOT_DIR = os.path.abspath(os.curdir)

utils_logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "utils.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.addHandler(console_handler)
utils_logger.setLevel(logging.DEBUG)


def get_json_transactions(filename: str = "") -> Any:
    """
    Функция, принимает на вход путь до JSON-файла и возвращает список словарей.
    Если файл пустой или не найден, функция возвращает пустой список.
    """
    try:
        utils_logger.info(f"attempt to open file {filename}")
        transactions = json.load(open(filename, encoding="utf-8"))
    except FileNotFoundError:
        utils_logger.error(f"get_json_transactions file {filename} not found")
        return []
    except json.decoder.JSONDecodeError:
        utils_logger.error("get_json_transactions JSON decode error")
        return []
    else:
        utils_logger.info("get_json_transactions successfully")
        return transactions


def get_transaction_amount(transaction: dict = {}) -> Any:
    """
    Функция, принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
     и возвращается конвертированная валюта в RUB.
    """
    utils_logger.info("get_transaction_amount attempt to receive transaction amount")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        utils_logger.info("get_transaction_amount successfully")
        return float(transaction["operationAmount"]["amount"])
    else:
        utils_logger.info("get_transaction_amount attempt to convert transaction amount")
        result = api.currency_conversion(transaction)
        utils_logger.info("get_transaction_amount successfully")
        return result
