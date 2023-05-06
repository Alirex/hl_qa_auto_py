"""
Написать функцию, которая принимает параметром функцию и произвольное число последовательностей.
Если передается одна последовательность, то надо вернуть список,
    в котором будет результат применения функции к каждому элементу последовательности.
Если передается несколько последовательностей, то переданная функция должна иметь такое же количество аргументов.
    В этом случае надо вернуть список, который будет состоять из результатов выполнения функции,
    в которую передали первые элементы всех последовательностей, затем вторые, и т. д.
Если переданные последовательности разной длины, то результат сформировать по кратчайшему.
Встроенную функцию map не использовать.



def custom_map(function, *sequences):
    pass

assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
"""
from typing import TypeVar
from collections.abc import Callable, Iterable

T = TypeVar("T")


def custom_map(function: Callable[[T, ...], T], *sequences: Iterable[T]) -> list[T]:
    return [function(*item) for item in zip(*sequences)]


def custom_map_2(function: Callable[[T, ...], T], *sequences: Iterable[T]) -> list[T]:
    result = []
    iterables = [iter(item) for item in sequences]

    while True:
        try:
            result.append(function(*[next(item) for item in iterables]))
        except StopIteration:
            break
    return result


def main() -> None:
    for action in [
        custom_map,
        custom_map_2,
    ]:
        print(f"{action.__name__=}")

        result_1 = action(sum, [[1, 2, 3], [4, 5]])
        print(f"{result_1=}")
        # noinspection Assert
        assert result_1 == [6, 9]
        result_2 = action(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44))
        print(f"{result_2=}")
        # noinspection Assert
        assert result_2 == [4, 6, 7, 8]


if __name__ == "__main__":
    main()
