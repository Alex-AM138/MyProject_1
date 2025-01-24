from unittest.mock import Mock, mock_open, patch

import pandas as pd
import pytest

import src.csv_and_excel_reader as reading


@patch("builtins.open", mock_open(read_data=None))
def test_csv_reading() -> None:
    mock_reader = Mock(
        return_value=[{"id": 1, "currency": 100}, {"id": 2, "currency": 200}, {"id": 3, "currency": 300}]
    )
    reading.csv.DictReader = mock_reader
    assert reading.csv_reading(csv_filepath=pd.DataFrame) == [
        {"id": 1, "currency": 100},
        {"id": 2, "currency": 200},
        {"id": 3, "currency": 300},
    ]
    assert reading.csv_reading(csv_filepath=pd.DataFrame)[1] == {"id": 2, "currency": 200}


def test_csv_reading_filepath() -> None:
    with pytest.raises(FileNotFoundError):
        reading.csv_reading("test_path")


def test_excel_reading() -> None:
    mock_reader = Mock(return_value=pd.DataFrame({"id": [1, 2, 3], "currency": [100, 200, 300]}))
    reading.pd.read_excel = mock_reader
    assert reading.excel_reading(excel_filepath=pd.DataFrame) == [
        {"id": 1, "currency": 100},
        {"id": 2, "currency": 200},
        {"id": 3, "currency": 300},
    ]
    assert reading.excel_reading(excel_filepath=pd.DataFrame)[1] == {"id": 2, "currency": 200}
