import re
import collections


def trans_search(transactions, string_search):
    '''
    принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка
    :param transactions:
    :param string_search:
    :return:
    '''
    list_result = []
    pattern = re.compile(re.escape(string_search), re.I)

    for transaction in transactions:
        description = transaction.get('description')
        if isinstance(description, str) and re.search(pattern, description):
            list_result.append(transaction)

    return list_result

def count_trans(list_trans, list_category):
    '''
    принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    :param list_trans:
    :param list_category:
    :return:
    '''
    count_operation = collections.Counter(list_trans)

    for trans in list_trans:
        description = trans.get('description').lower()

        for category in list_category:
            if category.lower() in description:
                count_operation[category] += 1

    return count_operation
