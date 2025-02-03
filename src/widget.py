import src.decorators as decorators
from src.masks import get_mask_account, get_mask_card_number


@decorators.log(filename="log.txt")  # type: ignore[operator]
def mask_account_card(input: str) -> str:
    """
    Функция принимает на вход строку, содержащую тип данных и номер карты или счёта
    и возвращает маскированный номер с типом данных
    """
    if "Счет" in input:
        return f"{input[0:len(input) - 20]}{get_mask_account(input[-20:])}"
    else:
        return f"{input[0:len(input) - 16]}{get_mask_card_number(input[-16:])}"


@decorators.log(filename="log.txt")  # type: ignore[operator]
def get_date(input_date: str) -> str:
    """
    Функция принимает на вход строку даты
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
    """

    splited_date = input_date.split("-")

    splited_date.reverse()

    splited_date[0] = splited_date[0][0:2]

    formated_date = ".".join(splited_date)

    return formated_date
