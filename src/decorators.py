from collections.abc import Callable


def log(filename: str = "") -> object:
    """
    Декоратор, который автоматически регистрирует детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках.
    """

    def decorator(func: Callable) -> object:
        def wrapper(*args: str, **kwargs: int) -> object:
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                try:
                    file = open(filename, "a")
                except FileNotFoundError:
                    print(f"{func.__name__} error: {err}, inputs: {args}, {kwargs}\n")
                else:
                    file.write(f"{func.__name__} error: {err}, inputs: {args}, {kwargs}\n")
                    file.close()
                raise Exception(f"Function error: {err}")
            else:
                try:
                    file = open(filename, "a")
                except FileNotFoundError:
                    print(f"{func.__name__} ok\n")
                else:
                    file.write(f"{func.__name__} ok\n")
                    file.close()
                return result

        return wrapper

    return decorator
