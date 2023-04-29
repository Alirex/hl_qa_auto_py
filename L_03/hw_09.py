"""
По введенному числу n, вывести паттерн из чисел

> Enter n: 2
  1
1 2 1
> Enter n: 5
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""
import contextlib
import itertools


@contextlib.contextmanager
def make_padding_dual_side(
    padding_size: int,
    #
    tile__background: str,
    tile__space: str,
):
    print(*([tile__space] * padding_size), sep=tile__background, end="")
    if padding_size:
        print(tile__background, end="")
    yield
    if padding_size:
        print(tile__background, end="")
    print(*([tile__space] * padding_size), sep=tile__background, end="")


def print_pattern(
    number: int,
    #
    tile__background: str = " ",
) -> None:
    zone_width = len(str(number))

    tile__space = tile__background * zone_width

    for i in range(1, number + 1):
        with make_padding_dual_side(
            padding_size=number - i,
            tile__background=tile__background,
            tile__space=tile__space,
        ):
            numbers = itertools.chain(
                range(1, i + 1),
                range(i - 1, 0, -1),
            )
            numbers_part = map(
                lambda number_: f"{number_:{tile__background}^{zone_width}}",
                numbers,
            )
            print(tile__background.join(numbers_part), end="")

        print()


def main() -> None:
    # print_pattern(
    #     number=111,
    #     # number=11,
    #     # number=9,
    #     #
    #     tile__background="-"
    # )

    number = int(input("Enter n: "))
    print_pattern(number=number)


if __name__ == "__main__":
    main()
