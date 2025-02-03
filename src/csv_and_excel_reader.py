import csv
import os

import pandas as pd

ROOT_DIR = os.path.abspath(os.pardir)


def csv_reader(filepath: str = "") -> list:
    """
    Функция принимает на вход путь к файлу формата 'csv', и возвращает список словарей
    с данными из файла.
    """
    try:
        with open(filepath, encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def excel_reader(filepath: str = "") -> pd.DataFrame:
    """
    Функция принимает на вход путь к файлу формата 'xlsx', и возвращает список словарей
    с данными из файла.
    """
    data = pd.read_excel(filepath).to_dict("records")
    return data