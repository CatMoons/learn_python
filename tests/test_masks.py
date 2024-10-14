import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "type_and_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("123456", "1234 56** **** "),
        ("1234567890123456789012", "1234 56** **** 3456789012")
    ],
)
def test_get_mask_card_number(type_and_number, expected):
    assert get_mask_card_number(type_and_number) == expected


@pytest.mark.parametrize(
    "type_and_number, expected",
    [("73654108430135874305", "**4305"), ("73654108430135877892", "**7892"), ("73654108430135871005", "**1005")],
)
def test_get_mask_account(type_and_number, expected):
    assert get_mask_account(type_and_number) == expected
