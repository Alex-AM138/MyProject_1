import csv
import pandas as pd
import os


ROOT_DIR = os.path.abspath(os.pardir)


def csv_reading(csv_filepath: str) -> list:
    """
    Функция для считывания финансовых операций из CSV принимает
    путь к файлу CSV в качестве аргумента и выдаёт список словарей с транзакциями.
    """
    try:
        with open(csv_filepath, mode='r', encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=', ')
            return list(reader)

    except Exception as e:
        print(f"Function error: {e}")


def excel_reading(excel_filepath: str) -> pd.DataFrame:
    """
    Функция для считывания финансовых операций из Excel.
    Функция принимает путь к файлу Excel в качестве аргумента,
    и выдаёт список словарей с транзакциями.
    """
    excel_data = pd.read_excel(excel_filepath).to_dict("records")
    return excel_data