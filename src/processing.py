def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    list_executed: list = []
    list_canceled: list = []
    for key in list_dictionary:
        if key.get("state") == state:
            list_executed.append(key)
        else:
            list_canceled.append(key)


    return f"{list_executed}\n{list_canceled}"


def sort_by_date(list_dictionary: list, sort_order: bool = True) -> list:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    sort_date = sorted(list_dictionary, key=lambda x: x["date"], reverse=sort_order)
    return sort_date