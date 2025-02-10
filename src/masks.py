def get_mask_card_number(number_card: str) -> str:
    """
    Функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.

    Пример ввода:
    1234567891234567

    Пример вывода:
    1234 56** **** 4567
    """

    str_number_card = str(number_card)
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


print(get_mask_card_number("1234567891234567"))


def get_mask_account(account: str) -> str:
    """
    Функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.

    Пример ввода:
    98765432198765432198

    Пример вывода:
    **2198
    """

    str_account = str(account)
    return f"**{str_account[-4:]}"


print(get_mask_account("98765432198765432198"))
