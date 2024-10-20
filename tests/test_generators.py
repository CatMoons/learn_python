from locale import currency
from typing import Generator

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions


def test_filter_by_currency():
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("name") == currency:
            usd_transactions = filter_by_currency(transactions, "USD")
            assert next(usd_transactions) == {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
            assert next(usd_transactions) == {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
            assert next(usd_transactions) == {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            }
        elif transaction.get("operationAmount").get("currency").get("name") != currency:
            assert StopIteration("Ошибка в данных!")


def test_transaction_descriptions():
    for transaction in transactions:
        if transaction.get("description") in transactions:
            assert next(transactions) == "Перевод организации"
            assert next(transactions) == "Перевод со счета на счет"
            assert next(transactions) == "Перевод со счета на счет"
            assert next(transactions) == "Перевод с карты на карту"
            assert next(transactions) == "Перевод организации"
        elif transactions == []:
            assert StopIteration


def test_card_number_generator():
    if card_number_generator(1, 6):
        assert next(card_number_generator(1, 5)) == "0000 0000 0000 0001"
        assert next(card_number_generator(2, 5)) == "0000 0000 0000 0002"
        assert next(card_number_generator(3, 5)) == "0000 0000 0000 0003"
        assert next(card_number_generator(4, 5)) == "0000 0000 0000 0004"
        assert next(card_number_generator(5, 5)) == "0000 0000 0000 0005"
