"""
Есть список из не менее, чем двух float элементов.

Создать новый список, в котором между элементами исходного списка будут добавлены их средние значения.


lst = [3.5, 2, 4, 6.2, 8] ->
[3.5, 2.75, 2, 3.0, 4, 5.1, 6.2, 7.1, 8]
"""


def get_new_list(
    lst: list[float],
) -> list[float]:
    new_list = []
    for index, item in enumerate(lst[:-1]):
        new_list.extend(
            (
                item,  # Current element
                (item + lst[index + 1]) / 2,  # Average between current and next element
            )
        )
    new_list.append(lst[-1])

    return new_list


def main() -> None:
    lst = [3.5, 2, 4, 6.2, 8]
    new_list = get_new_list(lst)
    print(new_list)


if __name__ == "__main__":
    main()
