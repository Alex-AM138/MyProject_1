def filter_by_state(list_of_dict: list, status_for_key: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и выводит новый список словарей, по указанному ключу 'state',
        если ключ не был дан на вход функции, будет выведен список по ключу по умолчанию"""
    new_list = []
    if status_for_key == 'EXECUTED':
        for state in list_of_dict:
            if state.get('state') == 'EXECUTED':
                new_list.append(state)
        return new_list
    elif status_for_key == 'CANCELED':
        for state in list_of_dict:
            if state.get('state') == 'CANCELED':
                new_list.append(state)
        return new_list
# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))

def sort_by_date():
    pass
