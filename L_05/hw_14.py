"""
Есть список состоящий из целых чисел. Создать три списка:

- в первый список добавить числа, которые делятся только на 3, но не на 5

- во второй список добавить числа, которые делятся только на 5, но не на 3

- в третий список добавить числа, которые делятся и на 3, и на 5



[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
[3, 6, 9, 12]  # elements divided by 3
[5, 10]  # elements divided by 5
[0, 15]  # elements divided by 3 and by 5
"""


def dispatcher(
    input_list: list[int],
) -> tuple[list[int], list[int], list[int]]:
    divided_by_3 = []
    divided_by_5 = []
    divided_by_3_and_5 = []

    for number in input_list:
        if not number % 3 and not number % 5:
            divided_by_3_and_5.append(number)
        elif not number % 3:
            divided_by_3.append(number)
        elif not number % 5:
            divided_by_5.append(number)

    return divided_by_3, divided_by_5, divided_by_3_and_5


def main() -> None:
    input_list = list(range(16))
    print(input_list)

    divided_by_3, divided_by_5, divided_by_3_and_5 = dispatcher(input_list)

    print(divided_by_3)
    print(divided_by_5)
    print(divided_by_3_and_5)


if __name__ == "__main__":
    main()
