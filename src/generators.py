from typing import Generator



def filter_by_currency(transactions: list, currency: str) -> Generator[list, None, None]:
    """
    Функция которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).

    """
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction



def transaction_descriptions(transactions: list) -> Generator[list, str, None]:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

    """
    for transaction in transactions:
        try:
            yield transaction.get("description")
        except StopIteration:
            break


def card_number_generator(start: int, end: int) -> Generator[str, str, None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """

    for number in range(start, end + 1):

        card_number = f"{number:016d}"

        formatted_card_number: str = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield formatted_card_number
