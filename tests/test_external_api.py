from unittest.mock import patch

import requests

import src.decorators as decorators
from src.external_api import currency_conversion


@decorators.log(filename="log.txt")
@patch("requests.request")
def test_currency_conversion(mock_get) -> None:
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 103.44, "from": "USD", "to": "RUB"},
        "result": 10343.8,
        "success": True,
    }

    requests.request = mock_get
    assert (
        currency_conversion({"operationAmount": {"amount": "103.44", "currency": {"name": "руб.", "code": "RUB"}}})
        == 10343.8
    )
    mock_get.assert_called_once()
