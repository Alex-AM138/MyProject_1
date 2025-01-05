import pytest

import src.decorators as decorators


def test_log_decorator_file_function_error() -> None:
    """
    Ошибочный тест декоратора и запись в файл
    """

    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    with pytest.raises(Exception):
        func(1, 1)


def test_log_decorator_file() -> None:
    """
    Успешно пройденный тест декоратора и запись в файл
    """

    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    result = func(2, 1)
    assert result == 1


def test_log_decorator_console_func_error() -> None:
    """
    Ошибочный тест декоратора и вывод в консоль
    """

    @decorators.log()
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    with pytest.raises(Exception):
        func(1, 1)


def test_log_decorator_console() -> None:
    """
    Успешно пройденный тест декоратора и вывод в консоль
    """

    @decorators.log()
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    result = func(2, 1)
    assert result == 1
