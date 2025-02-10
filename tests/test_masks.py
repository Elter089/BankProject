from unittest import expectedFailure

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_string_input():
    """Тест с корректным строковым вводом"""
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"


def test_get_mask_card_number_different_types():
    """Тест с различными типами входных данных"""
    test_cases = [
        "1234567891234567",
        1234567891234567
    ]

    expected_masks = [
        "1234 56** **** 4567",
        "1234 56** **** 4567"
    ]

    for input_value, expected_mask in zip(test_cases, expected_masks):
        assert get_mask_card_number(input_value) == expected_mask


def test_get_mask_account_string_input():
    """Тест с корректным строковым вводом"""
    assert get_mask_account("98765432198765432198") == "**2198"


def test_get_mask_account_different_types():
    """Тест с различными типами входных данных"""
    test_cases = [
        "98765432198765432198",
        98765432198765432198,
        "12345678901234567890"
    ]

    expected_masks = [
        "**2198",
        "**2198",
        "**7890"
    ]

    for input_value, expected_mask in zip(test_cases, expected_masks):
        assert get_mask_account(input_value) == expected_mask


@pytest.mark.parametrize("card_number, expected_output", [
    ("1234567891234567", "1234 56** **** 4567"),
    ("4444444444444444", "4444 44** **** 4444"),
    ("5555555555554444", "5555 55** **** 4444"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("9999888877776666", "9999 88** **** 6666")
])
def test_valid_card_numbers(card_number, expected_output):
    """Тест для проверки корректной маскировки валидных номеров карт"""
    assert get_mask_card_number(card_number) == expected_output


@pytest.mark.parametrize("account_number, expected_output", [
    ("98765432198765432198", "**2198"),
    ("12345678901234567890", "**7890"),
    ("00000000000000000000", "**0000"),
    ("11111111111111111111", "**1111"),
    ("99999999999999999999", "**9999")
])
def test_valid_account_numbers(account_number, expected_output):
    """Тест для проверки корректной маскировки валидных номеров счетов"""
    assert get_mask_account(account_number) == expected_output


def test_short_account_number():
    """Тест проверяет маскировку короткого номера счета"""
    assert get_mask_account("1234") == "**1234"


def test_valid_account_number():
    """Тест проверяет корректную маскировку стандартного номера счета"""
    assert get_mask_account("98765432198765432198") == "**2198"


def test_minimum_length():
    """Тест проверяет работу с минимально допустимой длиной"""
    assert get_mask_account("1") == "**1"


def test_typical_account_numbers():
    """Тест проверяет работу с типичными номерами счетов"""
    test_cases = [
        ("40817810099910004312", "**4312"),
        ("30232810600000000001", "**0001"),
        ("20202810100000000007", "**0007")
    ]
    for account, expected in test_cases:
        assert get_mask_account(account) == expected


def test_all_zeros():
    """Тест проверяет маскировку номера счета, состоящего из нулей"""
    assert get_mask_account("00000000000000000000") == "**0000"


def test_get_mask_card_number_basic():
    """Тест базового случая с 16-значным номером карты"""
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"


def test_get_mask_card_number_different_numbers():
    """Тест различных комбинаций номеров карт"""
    test_cases = [
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("0000000000000000", "0000 00** **** 0000")
    ]
    for input_number, expected in test_cases:
        assert get_mask_card_number(input_number) == expected


def test_get_mask_card_number_with_integer():
    """Тест работы функции с целочисленным входным значением"""
    assert get_mask_card_number(1234567891234567) == "1234 56** **** 4567"


