"""
Написать функцию, которая принимает несколько последовательностей,
    и возвращает список из кортежей составленных из элементов последовательностей одного индекса.

Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" послдовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default

Встроенную функцию zip не использовать.


def custom_zip(*sequences, full=False, default=None):
    pass

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
"""

import itertools
from collections.abc import Iterable
from typing import Any, TypeAlias

T_ITEM: TypeAlias = Any


def custom_zip(
    *sequences: Iterable[T_ITEM],
    #
    full: bool = False,
    default: T_ITEM | None = None,
) -> list[tuple[T_ITEM, ...]]:
    result = []

    iterables = []
    for sequence in sequences:
        iterable = iter(sequence)
        iterables.append(iterable)

    iterables_left_count = len(iterables)
    while True:
        try:
            _temp_container = []
            for index, iterable in enumerate(iterables):
                try:
                    data = next(iterable)
                except StopIteration:
                    if full:
                        iterables_left_count -= 1

                        if not iterables_left_count:
                            raise

                        iterables[index] = itertools.repeat(default)
                        data = default
                    else:
                        raise
                _temp_container.append(data)
        except StopIteration:
            break

        result.append(tuple(_temp_container))

    return result


def main() -> None:
    seq1 = [1, 2, 3, 4, 5]
    seq2 = [9, 8, 7]
    # noinspection Assert
    assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
    # noinspection Assert
    assert custom_zip(seq1, seq2, full=True, default="Q") == [
        (1, 9),
        (2, 8),
        (3, 7),
        (4, "Q"),
        (5, "Q"),
    ]


if __name__ == "__main__":
    main()
