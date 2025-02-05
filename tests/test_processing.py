import pytest

from src.processing import filter_by_state, sorted_by_date


@pytest.mark.parametrize("test_input, state, expected", [
    # Тест с разными состояниями
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "EXECUTED"}
        ],
        "EXECUTED",
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"}
        ]
    ),
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "PENDING"}
        ],
        "CANCELED",
        [
            {"id": 2, "state": "CANCELED"}
        ]
    ),
    # Тест с пустым списком
    (
        [],
        "EXECUTED",
        []
    ),
    # Тест с несуществующим состоянием
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"}
        ],
        "NON_EXISTENT",
        []
    ),
    # Тест со смешанными состояниями
    (
        [
            {"id": 1, "state": "PENDING"},
            {"id": 2, "state": "PENDING"},
            {"id": 3, "state": "EXECUTED"}
        ],
        "PENDING",
        [
            {"id": 1, "state": "PENDING"},
            {"id": 2, "state": "PENDING"}
        ]
    )
])
def test_filter_by_state(test_input, state, expected):
    """
    Параметризированный тест функции filter_by_state
    :param test_input: входной список словарей
    :param state: состояние для фильтрации
    :param expected: ожидаемый результат
    """
    assert filter_by_state(test_input, state) == expected


@pytest.mark.parametrize("test_input, expected", [
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"},
            {"id": 3, "state": "EXECUTED"}
        ],
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"}
        ]
    ),
    (
        [],
        []
    )
])
def test_filter_by_state_default(test_input, expected):
    """
    Параметризированный тест функции filter_by_state со значением по умолчанию
    :param test_input: входной список словарей
    :param expected: ожидаемый результат
    """
    assert filter_by_state(test_input) == expected


@pytest.mark.parametrize("test_input, sort_order, expected", [
    # Тест сортировки по убыванию (reverse=True)
    (
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-14T15:30:00.000"},
            {"id": 3, "date": "2023-07-16T08:45:00.000"}
        ],
        True,
        [
            {"id": 3, "date": "2023-07-16T08:45:00.000"},
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-14T15:30:00.000"}
        ]
    ),
    # Тест сортировки по возрастанию (reverse=False)
    (
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-14T15:30:00.000"},
            {"id": 3, "date": "2023-07-16T08:45:00.000"}
        ],
        False,
        [
            {"id": 2, "date": "2023-07-14T15:30:00.000"},
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 3, "date": "2023-07-16T08:45:00.000"}
        ]
    ),
    # Тест с пустым списком
    (
        [],
        True,
        []
    ),
    # Тест с одним элементом
    (
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"}
        ],
        True,
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"}
        ]
    ),
    # Тест с одинаковыми датами
    (
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-15T10:00:00.000"},
            {"id": 3, "date": "2023-07-15T10:00:00.000"}
        ],
        True,
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-15T10:00:00.000"},
            {"id": 3, "date": "2023-07-15T10:00:00.000"}
        ]
    )
])
def test_sorted_by_date(test_input, sort_order, expected):
    """
    Параметризированный тест функции sorted_by_date
    :param test_input: входной список словарей
    :param sort_order: порядок сортировки (True - по убыванию, False - по возрастанию)
    :param expected: ожидаемый результат
    """
    assert sorted_by_date(test_input, sort_order) == expected


@pytest.mark.parametrize("test_input, expected", [
    (
        [
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-14T15:30:00.000"},
            {"id": 3, "date": "2023-07-16T08:45:00.000"}
        ],
        [
            {"id": 3, "date": "2023-07-16T08:45:00.000"},
            {"id": 1, "date": "2023-07-15T10:00:00.000"},
            {"id": 2, "date": "2023-07-14T15:30:00.000"}
        ]
    ),
    (
        [],
        []
    )
])
def test_sorted_by_date_default(test_input, expected):
    """
    Параметризированный тест функции sorted_by_date со значением по умолчанию
    :param test_input: входной список словарей
    :param expected: ожидаемый результат
    """
    assert sorted_by_date(test_input) == expected


