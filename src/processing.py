def filter_by_state(list_of_dicts: list, status_for_key: str = "EXECUTED") -> list:
    """Функция принимает список словарей и выводит новый список словарей, по указанному ключу 'state',
    если ключ не был дан на вход функции, будет выведен список по ключу по умолчанию"""
    new_list = []
    for state in list_of_dicts:
        if state.get("state") == status_for_key:
            new_list.append(state)
    return new_list


def sort_by_date(list_of_dicts: list, ascending: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию - убывание) и возвращает новый список отсортированный по дате"""
    new_list = [sorted(list_of_dicts, key=lambda date: date.get("date", 0), reverse=ascending)]
    return new_list
