"""
Написать функцию, на вход которой передают список чисел, а возвращает второе по величине число.

Если передали пустой список, функция должна вернуть None.

Из встроенных функций можно использовать только range и len.

Написать реализацию, которая выполняет только один проход списка.



def second_largest_number(lst):
    pass

second_largest_number([4, 2, 1, 5, 2, 5, 7])  # 5
second_largest_number([])  # None
"""


def second_largest_number(lst: list) -> int | None:
    if not lst:
        return None

    largest = lst[0]
    second_largest = None

    for index in range(1, len(lst)):
        number = lst[index]

        if number > largest:
            second_largest = largest
            largest = number

        elif (second_largest is None and number < largest) or (
            second_largest is not None and largest > number > second_largest
        ):
            second_largest = number
    return second_largest


def main() -> None:
    print(second_largest_number([4, 2, 1, 5, 2, 5, 7]))
    print(second_largest_number([]))

    # What if list contains only one element? Return None or that element? Now -> None
    print(
        second_largest_number(
            [
                2,
            ]
        )
    )

    # What if list contains two same biggest elements? Return biggest element or "next biggest but less than biggest"?
    # Now -> "next biggest but less than biggest"
    print(second_largest_number([7, 2, 7]))


if __name__ == "__main__":
    main()
