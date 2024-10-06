def get_mask_card_number(number_card: str) -> str:
    """Функция которая принимает на вход номер карты и возвращает ее маску."""

    return f"{number_card[:4]} {number_card[5:7]}** **** {number_card[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция которая принимает номер аккаунта и возвращает его маску."""

    return f"**{account_number[-4:]}"
