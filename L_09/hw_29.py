"""
Линеаризация списка
Есть список, в котором могут быть числа и вложенные списки, в которых могут быть числа и вложенные списки, в которых...
Написать функцию, которая на вход принимает такой список, а возвращает плоский список из всех вложеных элементов
P.S. Преобразовать в строку функцией str удалить квадратные скобки и запятые, а потом разбить по пробелам - нельзя)



def linearize_list(lst):
    pass

lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
linearize_list(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""
from collections import deque
from typing import TypeAlias, Union

T_NUMBERS: TypeAlias = list[int]
T_NESTED_LIST_WITH_POSSIBLE_NESTED_LISTS: TypeAlias = list[
    Union[int, "T_NESTED_LIST_WITH_POSSIBLE_NESTED_LISTS"]
]


def linearize_list(
    lst: T_NESTED_LIST_WITH_POSSIBLE_NESTED_LISTS,
) -> T_NUMBERS:
    # Can have problems with recursion depth.
    result: T_NUMBERS = []

    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_list(item))
        else:
            result.append(item)

    return result


def linearize_list_by_deque(
    lst: T_NESTED_LIST_WITH_POSSIBLE_NESTED_LISTS,
) -> T_NUMBERS:
    # Without recursion.

    result: T_NUMBERS = []

    local_deque = deque()
    local_deque.extend(lst)

    while local_deque:
        item = local_deque.popleft()
        if isinstance(item, list):
            local_deque.extendleft(reversed(item))
        else:
            result.append(item)

    return result


def get_lst() -> T_NESTED_LIST_WITH_POSSIBLE_NESTED_LISTS:
    return [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]


example_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def main() -> None:
    lst = get_lst()
    print(f"{lst=}")
    print(f"{example_lst=}")

    for action in (
        linearize_list,
        linearize_list_by_deque,
    ):
        action_name = action.__name__
        result = action(lst)
        print(f"{action_name=}. Result: {result}")
        # noinspection Assert
        assert result == example_lst, f"{action_name=}. Result is not equal to example."


if __name__ == "__main__":
    main()
