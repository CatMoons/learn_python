from src.generators import filter_by_currency
import pytest

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "USD"
            }
        }
    },
    {
        "id": 2,
        "operationAmount": {
            "amount": 200.0,
            "currency": {
                "code": "EUR"
            }
        }
    },
    {
        "id": 3,
        "operationAmount": {
            "amount": 300.0,
            "currency": {
                "code": "USD"
            }
        }
    }
]

def test_filter_by_currency_usd():
    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    expected_transactions = [
        {
            "id": 1,
            "operationAmount": {
                "amount": 100.0,
                "currency": {
                    "code": "USD"
                }
            }
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": 300.0,
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]

    assert filtered_transactions == expected_transactions

def test_filter_by_currency_eur():
    filtered_transactions = list(filter_by_currency(transactions, "EUR"))
    expected_transactions = [
        {
            "id": 2,
            "operationAmount": {
                "amount": 200.0,
                "currency": {
                    "code": "EUR"
                }
            }
        }
    ]

    assert filtered_transactions == expected_transactions

def test_filter_by_currency_non_existent():
    filtered_transactions = list(filter_by_currency(transactions, "GBP"))
    assert filtered_transactions == []

if __name__ == "__main__":
    pytest.main()