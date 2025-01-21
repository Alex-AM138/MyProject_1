import logging
import os

ROOT_DIR = os.path.abspath(os.curdir)

masks_logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(f"{ROOT_DIR}/logs/masks.log", "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.addHandler(console_handler)
masks_logger.setLevel(logging.DEBUG)



# Реализация первой функции
def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты, заменяя цифры на '*'"""
    try:
        masks_logger.info("get_mask_card_number attempt to disguise number")
        result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    except Exception:
        masks_logger.error("get_mask_card_number {Exception}")
        raise Exception(f"{Exception}")
    if len(card_number) != 16 or not card_number.isdigit():
        masks_logger.error("get_mask_card_number format error")
        raise Exception("format error")
    else:
        masks_logger.info("get_mask_card_number successfully")
        return result


# Реализация второй функции
def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер аккаунта, заменяя цифры на '*'"""
    try:
        masks_logger.info("get_mask_card_number attempt to disguise number")
        result = "**" + account_number[-4:]
    except Exception:
        masks_logger.error(f"get_mask_account {Exception}")
        raise Exception(f"{Exception}")
    if len(account_number) != 20 or not account_number.isdigit():
        masks_logger.error("get_mask_account format error")
        raise Exception("format error")
    else:
        masks_logger.info("get_mask_account successfully")
        return result
