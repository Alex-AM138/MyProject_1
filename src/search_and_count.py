import collections
import logging
import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

se_logger = logging.getLogger("search_engine")
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "search_engine.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
se_logger.addHandler(file_handler)
se_logger.addHandler(console_handler)
se_logger.setLevel(logging.DEBUG)


def transaction_search(transactions: list = [], query: str = "") -> list:
    """
    Функция для поиска в списке словарей операций по заданной строке - описанию.
    Принимает два аргумента: список с транзакциями и строку для поиска.
    И возвращает список словарей с операциями, у которых в описании есть строка,
    переданная аргументу функции.
    """
    se_logger.debug(f"inputs: {transactions} {query}")
    find_transactions = []
    for transaction in transactions:
        description = transaction.get("description")
        if re.search(query, description, flags=re.IGNORECASE) is not None:
            find_transactions.append(transaction)
    se_logger.info("transaction_search successfully")
    se_logger.debug(f"result: {find_transactions}")
    return find_transactions


def category_count(transactions: list = [], categories: list = []) -> dict:
    """
    Функция для подсчёта количества банковских операций определенного типа.
    Принимает два аргумента: список с транзакциями и словарь для подсчёта транзакций по описанию.
    И возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    transaction_categories = []
    for transaction in transactions:
        try:
            if transaction["description"] in categories:
                transaction_categories.append(transaction["description"])
        except KeyError:
            se_logger.error("transaction format error")
            continue
    transaction_categories.extend(categories)
    result = collections.Counter(transaction_categories)
    result.subtract(categories)
    se_logger.info("category_count successfully")
    return dict(result)
