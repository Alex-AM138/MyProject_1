import json

import src.external_api as api_exchange

import  src.decorators as decorator


@decorator.log(filename='log.txt')
def get_json(filename: str) -> dict:
    """Функция чтения и получения данных из JSON-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            currency_transactions = json.load(f)
        return currency_transactions
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

@decorator.log(filename='log.txt')
def get_amount(transaction: dict) -> float:
    """Функция возвращает конвертированную сумму в RUB """
    try:
        if transaction['operationAmount']['currency'] == 'RUB':
            return float(transaction['operationAmount']['amount'])
        else:
            amount = float(transaction['operationAmount']['amount'])
            currency = transaction['operationAmount']['currency']
            return api_exchange.currency_conversion(amount, currency)
    except (KeyError, ValueError, TypeError) as e:
        print(f'Ошибка при получении транзакции: {e}')
