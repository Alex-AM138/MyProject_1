import pytest

import src.widget as widget


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert widget.mask_account_card(value) == expected


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(date: str) -> None:
    assert widget.get_date(date) == "11.03.2024"
