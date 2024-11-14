from src.generators import card_number_generator
import pytest

def test_card_number_format():
    start = 1
    end = 1
    result = next(card_number_generator(start, end))
    assert result == "0000 0000 0000 0001"

def test_card_number_count():
    start = 1
    end = 3
    result = list(card_number_generator(start, end))
    assert len(result) == 3

def test_card_number_range():
    start = 1
    end = 2
    result = list(card_number_generator(start, end))
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002"]

def test_large_numbers():
    start = 9999999999999998
    end = 9999999999999999
    result = list(card_number_generator(start, end))
    assert result == ["9999 9999 9999 9998", "9999 9999 9999 9999"]

def test_single_large_number():
    start = 9999999999999999
    end = 9999999999999999
    result = list(card_number_generator(start, end))
    assert result == ["9999 9999 9999 9999"]

def test_invalid_range():
    start = 10
    end = 5
    result = list(card_number_generator(start, end))
    assert result == []  # пустой список, так как нет валидного диапазона
