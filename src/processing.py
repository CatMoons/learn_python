def filter_by_state(list_dictionary: list, state: str = 'EXECUTED') -> list:
    list_executed = []
    lrst_canceled = []
    for key in list_dictionary:
        if key.get('state') == state:
            list_executed.append(key)
        else:
            lrst_canceled.append(key)
    return f"{list_executed}\n{lrst_canceled}"





def sort_by_date(list_dictionary: list, sort_order: bool = True) -> list:
    sort_date = sorted(list_dictionary, key=lambda x: x['date'], reverse=sort_order)
    return sort_date




