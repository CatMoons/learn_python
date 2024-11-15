from src.widget import mask_account_card
import pytest

def test_mask_account_card():
    # Тест на маскировку карты
    card_input = "Visa1234567812345678"
    expected_card_output = "Visa1234 56** **** 5678"
    assert mask_account_card(card_input) == expected_card_output

    # Тест на маскировку счета
    account_input = "Счет123456789"
    expected_account_output = "Счет 6789"
    assert mask_account_card(account_input) == expected_account_output

