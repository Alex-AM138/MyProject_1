import pytest

import src.search_and_count as se


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {"id": "1", "description": "Перевод организации"},
                {"id": "2", "description": "Открытие вклада"},
                {"id": "3", "description": "Перевод с карты на карту"},
                {"id": "4", "description": "Открытие вклада"},
            ],
            [
                {"id": "1", "description": "Перевод организации"},
                {"id": "3", "description": "Перевод с карты на карту"},
            ],
        )
    ],
)
def test_transaction_search(value, expected):
    assert se.transaction_search(value, "перевод") == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {"id": "1", "description": "Перевод организации"},
                {"id": "2", "description": "Открытие вклада"},
                {"id": "3", "description": "Перевод с карты на карту"},
                {"id": "4", "description": "Открытие вклада"},
            ],
            {"Перевод организации": 1, "Перевод с карты на карту": 1},
        )
    ],
)
def test_category_count(value, expected):
    assert se.category_count(value, ["Перевод организации", "Перевод с карты на карту"]) == expected
