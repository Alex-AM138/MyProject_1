import logging


def log(func, *, filename=None):
     if func is None:
         return lambda func: log(func, filename=filename)
     logger = logging.getLogger(func.__name__)
     logger.setLevel(logging.INFO)
     handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
     formatter = logging.Formatter('%(message)s')
     handler.setFormatter(formatter)
     logger.addHandler(handler)
     def wrapper(*args, **kwargs):
         try:
             logger.info(f"Вызов функции '{func.__name__}' с аргументами {args} и ключевыми аргументами {kwargs}")
             result = func(*args, **kwargs)
             logger.info(f"Функция '{func.__name__} OK")
             return result
         except Exception as n:
             logger.error(f"Функция '{func.__name__}' error: {type(n).__name__}. Inputs: {args}, {kwargs}")
             raise
     return wrapper
