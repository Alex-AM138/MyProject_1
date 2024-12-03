from src.masks import get_mask_card_number, get_mask_account


if __name__ == "__main__":
    print(get_mask_card_number("Visa Gold 5999414228426353"))
    print(get_mask_account("Счет 73654108430135874305"))
