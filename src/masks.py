# Реализация первой функции
def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты, заменяя цифры на '*'"""
    return card_number[-16:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]


# Реализация второй функции
def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер аккаунта, заменяя цифры на '*'"""
    return "**" + account_number[-4:]
