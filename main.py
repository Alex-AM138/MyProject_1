import logging
import os
from pathlib import Path

import src.csv_and_excel_reader as db
import src.generators as generators
import src.processing as processing
import src.search_and_count as se
import src.utils as utils
import src.widget as widget

ROOT_DIR = Path(__file__).resolve().parent.parent
TRANSACTIONS_JSON_PATH = os.path.join("X:\\MyProject1\\", "data", "operations.json")
TRANSACTIONS_CSV_PATH = os.path.join("X:\\MyProject1\\", "data", "transactions.csv")
TRANSACTIONS_XLSX_PATH = os.path.join("X:\\MyProject1\\", "data", "transactions_excel.xlsx")

main_logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "main.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
main_logger.addHandler(file_handler)
main_logger.addHandler(console_handler)
main_logger.setLevel(logging.DEBUG)


def user_input(input_value: str = "", parameters: list = []) -> str:
    """
    :param input_value: строка входных данных, вводимая пользователем
    :param parameters: список доступных команд
    :return: при совпадении ввода и списка команд возвращается введенная команда
    """
    main_logger.debug(f"{input_value}, {parameters}")
    parameters = [s.upper() for s in parameters]

    while input_value not in parameters:
        input_value = str(input("Пользователь: ")).upper()
        main_logger.info(f"Введено: {input_value}")
        if input_value in parameters:
            main_logger.info("Правильный ввод")
        else:
            main_logger.info("Неверный ввод")
            print("Программа: Неизвестная команда. Попробуйте еще раз.")
    return str(input_value)


def main():
    """
    Основная функция программы. Запрашивает у пользователя команды и возвращает отсортированный
    и отфильтрованный список в соответствии с параметрами, которые задал пользователь.
    """

    file_type = ""

    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )

    command = user_input("", ["1", "2", "3"])

    if command == "1":
        print("Для обработки выбран JSON-файл")
        file_type = "json"
    elif command == "2":
        print("Для обработки выбран CSV-файл")
        file_type = "csv"
    elif command == "3":
        print("Для обработки выбран XLSX-файл")
        file_type = "xlsx"

    state = ""
    while state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = str(input("Пользователь: ")).upper()
        main_logger.info(f"Введено: {state}")
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            main_logger.info("Правильный ввод")
        else:
            main_logger.info("Неверный ввод")
            print(f'Программа: Статус операции "{state}" недоступен.')

    transactions = []
    try:
        if file_type == "json":
            main_logger.info("try get transactions from json")
            transactions = utils.get_json_transactions(TRANSACTIONS_JSON_PATH)
        elif file_type == "xlsx":
            main_logger.info("try get transactions from xlsx")
            transactions = db.excel_reader(TRANSACTIONS_XLSX_PATH)
        elif file_type == "csv":
            main_logger.info("try get transactions from csv")
            transactions = db.csv_reader(TRANSACTIONS_CSV_PATH)
    except Exception:
        main_logger.error("get transactions error")

    main_logger.info(f"try filter by {state}")
    try:
        transactions = processing.filter_by_state(list(transactions), state)
    except Exception:
        main_logger.error("filtration error")

    print(f"Программа: Операции отфильтрованы по статусу '{state}'")

    print("Программа: Отсортировать операции по дате? Да/Нет")
    sorting_by_date = user_input("", ["да", "нет"])
    if sorting_by_date.lower() == "да":
        main_logger.info("try sorting by date")
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        sorting_param = user_input("", ["по возрастанию", "по убыванию"])
        main_logger.info("attempt to sort in descending / ascending order")
        transactions = processing.sort_by_date(transactions, sorting_param.lower() == "по убыванию")

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    currency_filter = user_input("", ["да", "нет"])
    if currency_filter.lower() == "да":
        main_logger.info("try filter by currencies")
        transactions = generators.filter_by_currency(transactions, "RUB")
        if transactions is None:
            main_logger.info("transactions not found by currencies")
        transactions_list = []
        for transaction in transactions:
            transactions_list.append(transaction)
        transactions_list = transactions_list[0]
    else:
        transactions_list = transactions

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    keyword_filter = user_input("", ["да", "нет"])
    if keyword_filter.lower() == "да":
        print("Программа: Введите слово для поиска.")
        keyword = input("Ввод: ")
        main_logger.info("try filter by keyword")
        transactions_list = se.transaction_search(transactions_list, keyword)
        if transactions_list is None:
            main_logger.info("transactions not found by keyword")

    return [transactions_list, file_type]


if __name__ == "__main__":
    program_data = main()  # получаем данные из основной функции
    transactions_list = program_data[0]  # итоговый список операций
    file_type = program_data[1]  # тип файла, с которым велась работа

    if transactions_list is None:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    print("Программа: Распечатываю итоговый список транзакций...")

    if len(transactions_list) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Программа: Всего банковских операций в выборке: {len(transactions_list)}")

    for transaction in transactions_list:
        print(f"{widget.get_date(transaction.get('date'))} {transaction.get('description')}")
        if transaction.get("description") == "Открытие вклада":
            print(f"{widget.mask_account_card(transaction.get('to'))}")
        else:
            print(
                f"{widget.mask_account_card(transaction.get('from'))} -> "
                f"{widget.mask_account_card(transaction.get('to'))}"
            )
            if file_type == "json":
                print(
                    f"{transaction.get('operationAmount').get('amount')}"
                    f"{transaction.get('operationAmount').get('currency').get('code')}"
                )
            else:
                print(f"{transaction.get('amount')} {transaction.get('currency_code')}")
