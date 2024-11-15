import pytest

from src.widget import get_date

def test_get_date_valid():
    '''
    тест с корректными форматами даты.
    :return:
    '''
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("1999-12-31T23:59:59.999999") == "31.12.1999"
    assert get_date("2000-01-01T00:00:00.000000") == "01.01.2000"


def test_get_date_edge_cases():
    '''
    проверяет работу с граничными значениями
    :return:
    '''
    assert get_date("2024-02-29T12:34:56.789101") == "29.02.2024"
    assert get_date("1900-01-01T00:00:00.000000") == "01.01.1900"