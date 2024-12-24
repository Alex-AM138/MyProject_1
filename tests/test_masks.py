import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> str:
    return "Maestro 1596837868705199"


def test_masks_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "Maestro 1596 83** **** 5199"


@pytest.fixture
def account_number() -> str:
    return "Счет 64686473678894779589"


def test_masks_account_number(account_number: str) -> None:
    assert get_mask_account(account_number) == "Счет **9589"
