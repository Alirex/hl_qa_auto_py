"""
Написать генераторную функцию, которая принимает два параметра m, n.

Генератор должен возвращать числа от 1 до n (включительно),
затем числа от 1 до n в квадрате, и так до степени m (включительно)


for i in generator(3, 4):
    print(i)
# 1, 2, 3, 4, 1, 4, 9, 16, 1, 8, 27, 64
"""

import itertools

from collections.abc import Generator, Iterator


# https://docs.python.org/3/library/typing.html#typing.Generator
def generator(m: int, n: int) -> Generator[int, None, None]:
    max_power = m
    max_base_number = n

    # sourcery skip: use-itertools-product
    for power in range(1, max_power + 1):
        for base_number in range(1, max_base_number + 1):
            yield base_number**power


def generator_2(*, max_base_number: int, max_power: int) -> Iterator[int]:
    for power, base_number in itertools.product(
        range(1, max_power + 1),
        range(1, max_base_number + 1),
    ):
        yield base_number**power


def main() -> None:
    for i in generator(3, 4):
        print(i)

    for i in generator_2(
        max_base_number=4,
        max_power=3,
    ):
        print(i)

    example = [1, 2, 3, 4, 1, 4, 9, 16, 1, 8, 27, 64]

    # noinspection Assert
    assert list(generator(3, 4)) == example
    # noinspection Assert
    assert (
        list(
            generator_2(
                max_base_number=4,
                max_power=3,
            )
        )
        == example
    )

    print(f"{__debug__=}")


if __name__ == "__main__":
    main()
