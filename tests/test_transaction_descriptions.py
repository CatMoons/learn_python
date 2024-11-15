import pytest

from src.generators import transaction_descriptions

def test_transaction_descriptions_standard_case():
    transactions = [
        {'description': 'Payment for services', 'amount': 100},
        {'description': 'Refund', 'amount': -20},
        {'description': 'Purchase', 'amount': 50}
    ]

    expected_descriptions = ['Payment for services', 'Refund', 'Purchase']

    result = list(transaction_descriptions(transactions))

    assert result == expected_descriptions

def test_transaction_descriptions_empty_list():
    transactions = []

    expected_descriptions = []

    result = list(transaction_descriptions(transactions))

    assert result == expected_descriptions

def test_transaction_descriptions_missing_description():
    transactions = [
        {'amount': 100},
        {'description': 'Refund'},
        {'description': 'Purchase', 'amount': 50}
    ]

    expected_descriptions = [None, 'Refund', 'Purchase']

    result = list(transaction_descriptions(transactions))

    assert result == expected_descriptions

def test_transaction_descriptions_none_description():
    transactions = [
        {'description': None, 'amount': 100},
        {'description': 'Refund'},
        {'description': 'Purchase', 'amount': 50}
    ]

    expected_descriptions = [None, 'Refund', 'Purchase']

    result = list(transaction_descriptions(transactions))

    assert result == expected_descriptions

if __name__ == "__main__":
    pytest.main()