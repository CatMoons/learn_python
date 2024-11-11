def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    new_list = []
    for key in list_dictionary:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(list_dictionary: list, sort_order: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    sort_date = sorted(list_dictionary, key=lambda x: x["date"], reverse=sort_order)
    return sort_date


