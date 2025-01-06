def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция выводит список словарей, ключ которых соответствует заданному значению"""

    new_list_dict = []
    for item_list in list_dict:
        if item_list["state"] == state:
            new_list_dict.append(item_list)
    return new_list_dict


def sorted_by_date(list_dict: list, sort: bool = True) -> list:
    """Функция возвращает отсортированный по дате список"""

    sorted_list_dict = sorted(list_dict, key=lambda i: i["date"], reverse=sort)
    return sorted_list_dict
