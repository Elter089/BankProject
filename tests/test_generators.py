import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_mixed(transactions_fixture):
    filtered = list(filter_by_currency(transactions_fixture, 'USD'))
    assert len(filtered) == 2
    assert all(t['operationAmount']['currency']['code'] == 'USD' for t in filtered)


def test_filter_by_currency_empty(empty_transactions_fixture):
    filtered = list(filter_by_currency(empty_transactions_fixture))
    assert len(filtered) == 0


def test_filter_by_currency_single(single_transaction_fixture):
    filtered = list(filter_by_currency(single_transaction_fixture, 'USD'))
    assert len(filtered) == 1
    assert filtered[0]['operationAmount']['currency']['code'] == 'USD'


def test_filter_by_currency_all_same(same_currency_transactions_fixture):
    filtered = list(filter_by_currency(same_currency_transactions_fixture, 'USD'))
    assert len(filtered) == 2
    assert all(t['operationAmount']['currency']['code'] == 'USD' for t in filtered)


def test_filter_by_currency_no_matches(transactions_fixture):
    filtered = list(filter_by_currency(transactions_fixture, 'GBP'))
    assert len(filtered) == 0


@pytest.mark.parametrize("transactions, currency", [
    ([], "USD"),
    ([], "EUR"),
    ([], "GBP")
])
def test_empty_transactions(transactions, currency):
    """
    Тест работы с пустым списком транзакций
    """
    result = list(filter_by_currency(transactions, currency))
    assert result == []


def test_single_transaction(single_transaction):
    descriptions = list(transaction_descriptions(single_transaction))
    assert descriptions == ['Coffee purchase']


def test_multiple_transactions(multiple_transactions):
    descriptions = list(transaction_descriptions(multiple_transactions))
    assert descriptions == ['Grocery shopping', 'Gas station', 'Restaurant bill']


def test_transactions_with_empty_description(transactions_with_empty_description):
    descriptions = list(transaction_descriptions(transactions_with_empty_description))
    assert descriptions == ['', 'Valid description', '']


@pytest.mark.parametrize("transactions, expected", [
    ([{'description': ''}, {'description': ''}], ['', '']),
    ([{'description': ''}, {'description': 'Valid'}, {'description': ''}], ['', 'Valid', '']),
])
def test_empty_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


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
