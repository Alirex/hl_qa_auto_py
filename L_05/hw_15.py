"""
Найти сумму и произведение элементов списка больше числа MIN (включительно) и меньше числа MAX (включительно).

Если таких элементов нет, вывести ноль и для суммы, и для произведения.


lst = [2, 4, 6, 2, 1, 1, 9, 4, 6], MIN = 3, MAX = 6
sum_ = 20, product = 576
"""


def get_sum_and_product(
    lst: list[int],
    min_: int,
    max_: int,
) -> tuple[int, int]:
    sum_ = 0
    product = 1

    if items := [number for number in lst if min_ <= number <= max_]:
        for number in items:
            sum_ += number
            product *= number
    else:
        sum_ = 0
        product = 0

    return sum_, product


def main() -> None:
    # lst = list(range(10, 20))
    lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
    MIN = 3
    MAX = 6

    sum_, product = get_sum_and_product(
        lst=lst,
        min_=MIN,
        max_=MAX,
    )

    print(f"{sum_=}, {product=}")


if __name__ == "__main__":
    main()
