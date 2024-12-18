from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция, которая принимает номер карты или счета в банке"""
    number = card_or_account_number.split()
    if len(number) > 2:
        return "Ошибка: неверный ввод"

    ident = " ".join(number[:-1])
    new_number = number[-1]

    if ident.lower().startswith("счет"):
        masked_number = get_mask_account(new_number)
        return f"{ident} **{masked_number}"
    else:
        masked_number = get_mask_card_number(new_number)
        return f"{ident} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате:
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    date = date_string.split("T")[0]
    day, month, year = date.split("-")
    return f"{day}.{month}.{year}"
