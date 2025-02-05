import pytest

from src.widget import mask_account_card, get_date, get_mask_card_number, get_mask_account


def test_mask_account_card_account_recognition():
    """
    Тест распознавания счета и применения соответствующей маски
    """
    account_inputs = [
        ("Счет 12345678901234567890", "Счет ****7890"),
        ("счет 98765432198765432198", "счет ****2198"),
        ("СЧЕТ 00000000000000000001", "СЧЕТ ****0001")
    ]

    for input_value, expected_output in account_inputs:
        result = mask_account_card(input_value)
        assert result == expected_output, f"Ошибка при маскировке счета: {input_value}"


def test_partial_input():
    # Тест для частичного ввода (без номера)
    input_data = "Счет"
    expected_output = " Счет ** **** Счет"
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("input_data, expected_output", [
    # Тесты для карт различных типов
    ("Visa Classic 1234567812345678", "Ошибка: неверный ввод"),
    ("Mastercard 1234567812345678", "Mastercard 1234 56** **** 5678"),
    ("Maestro 1234567812345678", "Maestro 1234 56** **** 5678"),

    # Тесты для счетов
    ("Счет 12345678901234567890", "Счет ****7890"),
    ("Счет 98765432109876543210", "Счет ****3210"),

    # Тесты с разными регистрами
    ("VISA 1234567812345678", "VISA 1234 56** **** 5678"),
    ("счет 12345678901234567890", "счет ****7890"),
])
def test_mask_account_card_valid_input(input_data, expected_output):
    """
    Тест для проверки корректной маскировки номеров карт и счетов
    """
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize("input_date,expected_output", [
    ("2024-03-11T02:26:18.671407", "2024.03.11"),
    ("2023-12-31T23:59:59.999999", "2023.12.31"),
    ("2025-01-01T00:00:00.000000", "2025.01.01"),
    ("2024-02-29T12:00:00.000000", "2024.02.29"),
    ("2000-01-01T00:00:00.000000", "2000.01.01"),
])
def test_valid_dates(input_date, expected_output):
    """Тест корректных дат"""
    assert get_date(input_date) == expected_output

