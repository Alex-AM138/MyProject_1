import logging
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

masks_logger = logging.getLogger("masks")
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "masks.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.addHandler(console_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(num: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маскированную версию
    в формате XXXX XX** **** XXXX.
    """
    try:
        masks_logger.info("get_mask_card_number attempt to disguise number")
        result = f"{num[:4]} {num[4:6]}** **** {num[-4:]}"
    except Exception:
        masks_logger.error("get_mask_card_number {Exception}")
        raise Exception(f"{Exception}")
    if len(num) != 16 or not num.isdigit():
        masks_logger.error("get_mask_card_number format error")
        raise Exception("format error")
    else:
        masks_logger.info("get_mask_card_number successfully")
        return result


def get_mask_account(num: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маскированную версию
    в формате **XXXX.
    """
    try:
        masks_logger.info("get_mask_card_number attempt to disguise number")
        result = "**" + num[-4:]
    except Exception:
        masks_logger.error(f"get_mask_account {Exception}")
        raise Exception(f"{Exception}")
    if len(num) != 20 or not num.isdigit():
        masks_logger.error("get_mask_account format error")
        raise Exception("format error")
    else:
        masks_logger.info("get_mask_account successfully")
        return result
