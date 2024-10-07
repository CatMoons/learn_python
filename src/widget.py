from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(type_number_card: str) -> str:
    """
    Функция принимает аргумент в виде строки,
    содержащей тип и номер карты или счета.
    Возвращает строку с замаскированым номером
    """
    if "Счет" in type_number_card:
        return "Счет " + get_mask_account(type_number_card)
    else:
        return type_number_card[:-16] + get_mask_card_number(type_number_card[-16:])


def get_date(date: str) -> str:
    """
    Функция принимает на вход строку с датой в формате
    <2024-03-11T02:26:18.671407> и возвращает строку
    с датой в формате <ДД.ММ.ГГГГ(11.03.2024)>
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
