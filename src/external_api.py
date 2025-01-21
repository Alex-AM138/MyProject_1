import os

import requests
from dotenv import load_dotenv

import src.decorators as decorators

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


@decorators.log(filename="log.txt")  # type: ignore[operator]
def currency_conversion(transaction: dict) -> float:
    """
    Функция возвращает сумму в рублях делая запрос через API
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    headers = {"apikey": API_KEY}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    response = requests.request("GET", url, headers=headers)
    result = response.json()

    return round(result.get("result"), 2)
