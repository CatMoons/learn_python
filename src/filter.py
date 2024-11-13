from typing import Generator


def filter_by_curr_csv(transactions: list, currency: str) -> Generator[list, None, None]:
    """
    Функция которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).

    """
    for transaction in transactions:
        if transaction.get("currency_code") == currency:
            yield transaction
