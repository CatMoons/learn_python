import pytest
from src.masks import get_mask_card_number  # Импортируйте функцию из вашего модуля


def test_get_mask_card_number_valid_input():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("9876543210987654") == "9876 54** **** 7654"

def test_get_mask_card_number_invalid_input():
    with pytest.raises(Exception):
        get_mask_card_number("")
        get_mask_card_number(123)

def test_get_mask_card_number_non_string_input():
    with pytest.raises(TypeError):
        get_mask_card_number(1234567812345678)
        get_mask_card_number(None)