import pytest
from src.search_trans import trans_search

def test_trans_search_with_matching_description():
    '''
    проверяет, что функция возвращает транзакции, в описании которых содержится искомая строка.
    :return:
    '''
    transactions = [
        {'id': 1, 'description': 'Payment for invoice #123'},
        {'id': 2, 'description': 'Grocery shopping at Store'},
        {'id': 3, 'description': 'Subscription renewal'}
    ]
    string_search = 'grocery'
    result = trans_search(transactions, string_search)
    expected = [{'id': 2, 'description': 'Grocery shopping at Store'}]
    assert result == expected

def test_trans_search_case_insensitive():
    '''
    убеждается, что поиск нечувствителен к регистру.
    :return:
    '''
    transactions = [
        {'id': 1, 'description': 'Payment for invoice #123'},
        {'id': 2, 'description': 'grocery shopping at Store'},
        {'id': 3, 'description': 'Subscription renewal'}
    ]
    string_search = 'GROCERY'
    result = trans_search(transactions, string_search)
    expected = [{'id': 2, 'description': 'grocery shopping at Store'}]
    assert result == expected

def test_trans_search_no_match():
    '''
    проверяет случай, когда ни одна транзакция не соответствует искомой строке.
    :return:
    '''
    transactions = [
        {'id': 1, 'description': 'Payment for invoice #123'},
        {'id': 2, 'description': 'Grocery shopping at Store'},
        {'id': 3, 'description': 'Subscription renewal'}
    ]
    string_search = 'rent'
    result = trans_search(transactions, string_search)
    expected = []
    assert result == expected

def test_trans_search_empty_transactions():
    '''
    проверяет поведение функции при пустом списке транзакций.
    :return:
    '''
    transactions = []
    string_search = 'anything'
    result = trans_search(transactions, string_search)
    expected = []
    assert result == expected

if __name__ == '__main__':
    pytest.main()
