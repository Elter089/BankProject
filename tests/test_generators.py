from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest

def test_filter_by_currency_simple(simple_transactions):
    """Тест фильтрации USD транзакций из смешанного списка"""
    result = list(filter_by_currency(simple_transactions, 'USD'))
    assert len(result) == 2
    assert all(t['currency'] == 'USD' for t in result)


def test_filter_by_currency_empty(empty_transactions):
    """Тест фильтрации пустого списка"""
    result = list(filter_by_currency(empty_transactions))
    assert len(result) == 0


def test_filter_by_currency_usd_only(usd_only_transactions):
    """Тест фильтрации списка, где все транзакции в USD"""
    result = list(filter_by_currency(usd_only_transactions))
    assert len(result) == 3
    assert all(t['currency'] == 'USD' for t in result)


def test_filter_by_currency_missing_currency(transactions_without_currency):
    """Тест фильтрации списка с отсутствующими валютами"""
    result = list(filter_by_currency(transactions_without_currency))
    assert len(result) == 2
    assert all(t['currency'] == 'USD' for t in result)


@pytest.mark.parametrize("currency,expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("JPY", 1),
    ("GBP", 0)
])
def test_filter_by_currency_parametrized(simple_transactions, currency, expected_count):
    """Параметризованный тест для разных валют"""
    result = list(filter_by_currency(simple_transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t['currency'] == currency for t in result)


def simple_transactions_tran_desc(simple_transactions):
    """Тест формирования описаний для простых транзакций"""
    descriptions = list(transaction_descriptions(simple_transactions))
    assert len(descriptions) == 2
    assert descriptions[0] == "1234 -> 100 USD"
    assert descriptions[1] == "5678 -> 200 EUR"


def empty_transactions_tran_desc(empty_transactions):
    """Тест обработки пустого списка транзакций"""
    descriptions = list(transaction_descriptions(empty_transactions))
    assert len(descriptions) == 0


def test_missing_fields(transactions_with_missing_fields):
    """Тест обработки транзакций с отсутствующими полями"""
    descriptions = list(transaction_descriptions(transactions_with_missing_fields))
    assert len(descriptions) == 3
    assert descriptions[0] == "1234 -> 100 None"
    assert descriptions[1] == "None -> 200 EUR"
    assert descriptions[2] == "5678 -> None USD"


def test_none_values(transactions_with_none_values):
    """Тест обработки транзакций с None значениями"""
    descriptions = list(transaction_descriptions(transactions_with_none_values))
    assert len(descriptions) == 3
    assert descriptions[0] == "None -> 100 USD"
    assert descriptions[1] == "5678 -> None EUR"
    assert descriptions[2] == "9012 -> 300 None"


@pytest.mark.parametrize("transaction,expected", [
    (
        {"account_id": "1234", "amount": 100, "currency": "USD"},
        "1234 -> 100 USD"
    ),
    (
        {"account_id": "", "amount": 0, "currency": ""},
        " -> 0 "
    ),
    (
        {},
        "None -> None None"
    )
])
def test_single_transaction_description(transaction, expected):
    """Параметризованный тест для отдельных транзакций"""
    description = next(transaction_descriptions([transaction]))
    assert description == expected


def test_small_range(small_range_params):
    """Тест генерации небольшого диапазона номеров"""
    generator = card_number_generator(
        small_range_params['start'],
        small_range_params['end']
    )
    result = list(generator)
    assert result == small_range_params['expected']


def test_single_number(single_number_params):
    """Тест генерации одного номера"""
    generator = card_number_generator(
        single_number_params['start'],
        single_number_params['end']
    )
    result = list(generator)
    assert result == single_number_params['expected']


def test_end_range(end_range_params):
    """Тест генерации номеров в конце диапазона"""
    generator = card_number_generator(
        end_range_params['start'],
        end_range_params['end']
    )
    result = list(generator)
    assert result == end_range_params['expected']


@pytest.mark.parametrize("start,end,expected_first,expected_last", [
    (1, 3, '0000 0000 0000 0001', '0000 0000 0000 0003'),
    (999, 1001, '0000 0000 0000 0999', '0000 0000 0000 1001'),
    (9999, 10001, '0000 0000 0000 9999', '0000 0000 0001 0001')
])
def test_card_number_generator_parametrized(start, end, expected_first, expected_last):
    """Параметризованный тест для различных диапазонов"""
    generator = card_number_generator(start, end)
    result = list(generator)
    assert result[0] == expected_first
    assert result[-1] == expected_last
    assert len(result) == end - start + 1
