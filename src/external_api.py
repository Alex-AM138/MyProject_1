import os
import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv('API_KEY')


def currency_conversion(currency:str, amount:[int, float]) -> float:
    """Функция конвертирует валюту из USD и EUR в RUB"""
    response = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}')
    return response['result']