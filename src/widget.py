from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(unidentified_string: str) -> str:
    """Функция принимает строку и маскирует ее в зависимости от данных строки"""
    if "Счет" in unidentified_string:
        return get_mask_account(unidentified_string)
    else:
        return get_mask_card_number(unidentified_string)


def get_date(date_string: str) -> str:
    """Функция принимает строку и возвращает строку в формате 'ДД.ММ.ГГГГ'"""
    return date_string[8:10] + "." + date_string[5:7] + "." + date_string[:4]
