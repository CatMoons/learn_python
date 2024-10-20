import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "type_and_number, expected",
    [
        ("Master Card 1234567890123456", "Master Card 1234 56** **** 3456"),
        ("Счет 73654108430135877892", "Счет **7892"),
        ("Tinkoff 736542141084301358710053214", "Tinkoff 736542141084301 35** **** 3214"),
        ("fwjfwhfklm;llqkpo2342", "fwjfwhfkl m;** **** 2342"),
    ],
)
def test_mask_account_card(type_and_number, expected):
    assert mask_account_card(type_and_number) == expected


@pytest.mark.parametrize(
    "type_and_number, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", ".."),
        ("gjwlfwmfw", "w.wm.gjwl"),
    ],
)
def test_get_date(type_and_number, expected):
    assert get_date(type_and_number) == expected
