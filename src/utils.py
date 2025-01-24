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
file_handler = logging.FileHandler(f"{ROOT_DIR}/logs/utils.log", "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.addHandler(console_handler)
utils_logger.setLevel(logging.DEBUG)


def get_json_transactions(filename: str = "") -> Any:
    """
    Функция, принимает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
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


def get_transaction_amount(transaction: dict = {}) -> float:
    """
    Функция, принимает на вход транзакцию и возвращает конвертированную сумму транзакции в рублях
    """
    utils_logger.info("get_transaction_amount attempt to receive transaction amount")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        utils_logger.info("get_transaction_amount successfully")
        return float(transaction["operationAmount"]["amount"])
    else:
        utils_logger.info("get_transaction_amount attempt to convert transaction amount")
        result = api.currency_conversion(transaction)
        return result
