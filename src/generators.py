def filter_by_currency(transactions, currency='USD'):
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions (list): Список словарей с транзакциями
        currency (str): Валюта для фильтрации (по умолчанию 'USD')

    Returns:
        filter: Итератор отфильтрованных транзакций
    """
    return filter(lambda x: x.get('currency') == currency, transactions)


def transaction_descriptions(transactions):
    """Принимает список транзакций,
    формирует строку описания ля каждой транзакции,
    возвращает описания по одному используя yield"""
    for transaction in transactions:
        yield (f"{transaction.get('account_id')} "
               f"-> {transaction.get('amount')} "
               f"{transaction.get('currency')}")


def card_number_generator(start=1, end=9999999999999999):
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start (int): Начальное значение (по умолчанию 1)
        end (int): Конечное значение (по умолчанию 9999999999999999)

    Yields:
        str: Номер карты в формате XXXX XXXX XXXX XXXX
    """
    for num in range(start, end + 1):
        # Преобразуем число в строку и добавляем нули в начало
        card_num = '0' * (16 - len(str(num))) + str(num)
        # Форматируем строку, добавляя пробелы каждые 4 цифры
        yield ' '.join(card_num[i:i + 4] for i in range(0, 16, 4))
