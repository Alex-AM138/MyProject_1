from unittest.mock import Mock, mock_open, patch

import pandas as pd
import pytest

import src.csv_and_excel_reader as reader


@patch("builtins.open", mock_open(read_data=None))
def test_csv_reader() -> None:
    mock_reader = Mock(
        return_value=[{"id": 1, "currency": 100}, {"id": 2, "currency": 200}, {"id": 3, "currency": 300}]
    )
    reader.csv.DictReader = mock_reader
    assert reader.csv_reader() == [{"id": 1, "currency": 100}, {"id": 2, "currency": 200}, {"id": 3, "currency": 300}]
    assert reader.csv_reader()[1] == {"id": 2, "currency": 200}


def test_csv_reader_filepath() -> None:
    with pytest.raises(FileNotFoundError):
        reader.csv_reader("test_path")


def test_excel_reader() -> None:
    mock_reader = Mock(return_value=pd.DataFrame({"id": [1, 2, 3], "currency": [100, 200, 300]}))
    reader.pd.read_excel = mock_reader
    assert reader.excel_reader() == [
        {"id": 1, "currency": 100},
        {"id": 2, "currency": 200},
        {"id": 3, "currency": 300},
    ]
    assert reader.excel_reader()[1] == {"id": 2, "currency": 200}