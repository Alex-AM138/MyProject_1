import pytest

import src.masks as masks


@pytest.fixture
def card_number() -> str:
    return "7000792289606361"


def test_mask_card_number(card_number: str) -> None:
    assert masks.get_mask_card_number(card_number) == "7000 79** **** 6361"
    with pytest.raises(Exception):
        masks.get_mask_card_number("")


@pytest.fixture
def account() -> str:
    return "73654108430135874305"


def test_mask_account(account: str) -> None:
    assert masks.get_mask_account(account) == "**4305"
    with pytest.raises(Exception):
        masks.get_mask_account("")
