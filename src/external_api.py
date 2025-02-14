import logging
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent

api_logger = logging.getLogger("utils")
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "api.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
api_logger.addHandler(file_handler)
api_logger.addHandler(console_handler)
api_logger.setLevel(logging.DEBUG)

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


# @decorators.log(filename="log.txt")  # type: ignore[operator]
def currency_conversion(transaction: dict) -> Any:
    """
    Функция принимает на вход словарь с информацией о банковской операции,
    делает запрос через внешний API и возвращает сумму в рублях.
    """
    if transaction.get("currency_code") is None:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    else:
        amount = float(transaction.get("amount"))
        currency = transaction.get("currency_code")

    headers = {"apikey": API_KEY}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    api_logger.debug(f"{result}\n")

    return round(result.get("result"), 2)
