import pytes
from src.filter import filter_by_curr_csv


def test_filter_by_curr_csv():
    """
    тест содержащий различные ситуации:
    - фильтрация по конкретной валюте
    - фильтрация по валюте, отсутствующей в данных
    - фильтрация с пустым списком транзакций
    :return:
    """
    transactions = [
        {"id": 1, "amount": 100, "currency_code": "USD"},
        {"id": 2, "amount": 200, "currency_code": "EUR"},
        {"id": 3, "amount": 300, "currency_code": "USD"},
        {"id": 4, "amount": 400, "currency_code": "GBP"},
    ]

    currency = "USD"
    expected_output = [
        {"id": 1, "amount": 100, "currency_code": "USD"},
        {"id": 3, "amount": 300, "currency_code": "USD"},
    ]

    result = list(filter_by_curr_csv(transactions, currency))

    assert result == expected_output

    currency = "JPY"
    expected_output = []

    result = list(filter_by_curr_csv(transactions, currency))

    assert result == expected_output

    transactions = []
    currency = "USD"
    expected_output = []

    result = list(filter_by_curr_csv(transactions, currency))

    assert result == expected_output


if __name__ == "__main__":
    pytest.main()
