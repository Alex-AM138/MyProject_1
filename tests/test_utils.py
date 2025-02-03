from unittest.mock import mock_open, patch

import pytest

from src.utils import get_json_transactions, get_transaction_amount


# Тест функции get_json_transactions при ошибке чтения файла
def test_get_json_transactions_file_err() -> None:
    assert get_json_transactions("") == []


# Тест функции get_json_transactions при чтении пустого файла
@patch("builtins.open", mock_open(read_data=None))
def test_get_json_transactions_empty_file() -> None:
    assert get_json_transactions() == []


# Данные для тестирования работы функции get_json_transactions и get_transactions_amount
data = """[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }]"""


# Тест функции get_json_transactions по типу выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_get_json_transactions_type() -> None:
    assert type(get_json_transactions()) is list


# Тест функции get_json_transactions на соответствие выходного значения
@patch("builtins.open", mock_open(read_data=data))
def test_get_json_transactions_result() -> None:
    assert get_json_transactions()[0]["operationAmount"]["amount"] == "31957.58"


# Тест функции get_transactions_amount на правильность работы в рублях
@patch("builtins.open", mock_open(read_data=data))
def test_get_transaction_amount_rub() -> None:
    transaction = get_json_transactions()[0]
    assert get_transaction_amount(transaction) == float(31957.58)


@pytest.fixture
def transaction() -> dict:
    return {"operationAmount": {"amount": "100", "currency": {"name": "USD.", "code": "USD"}}}


# Тест функции get_transactions_amount на конвертацию валют
@patch("requests.request")
def test_get_transaction_amount_usd(mock_currency: None, transaction: dict) -> None:
    mock_currency.return_value.json.return_value = {"result": 10343.8}
    assert get_transaction_amount(transaction) == float(10343.8)
