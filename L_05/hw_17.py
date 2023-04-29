"""
Есть двумерный список из латинских букв, отсортировать буквы по колонкам.

Считаем, что список прямоугольный.



[['a', 'c', 'd']
 ['f', 'b', 'a']
 ['a', 'n', 'k']
 ['e', 'l', 'i']]
->
[['a', 'b', 'a']
 ['a', 'c', 'd']
 ['e', 'l', 'i']
 ['f', 'n', 'k']]
"""


def sort_by_columns__by_functions(
    matrix: list[list[str]],
) -> list[list[str]]:
    return list(
        map(
            list,
            zip(
                *map(
                    sorted,
                    zip(
                        *matrix,
                    ),
                ),
            ),
        ),
    )


def sort_by_columns__detailed(
    matrix: list[list[str]],
) -> list[list[str]]:
    columns_as_rows = zip(
        *matrix,
    )

    sorted_columns_as_rows = map(
        sorted,
        columns_as_rows,
    )

    sorted_columns_as_rows_as_columns = zip(
        *sorted_columns_as_rows,
    )

    return list(
        map(
            list,
            sorted_columns_as_rows_as_columns,
        ),
    )


def main() -> None:
    matrix = [
        ["a", "c", "d"],
        ["f", "b", "a"],
        ["a", "n", "k"],
        ["e", "l", "i"],
    ]

    print("Before:")
    for row in matrix:
        print(row)

    print("After:")
    for row in sort_by_columns__by_functions(matrix):
        print(row)

    print("After (2):")
    for row in sort_by_columns__detailed(matrix):
        print(row)


if __name__ == "__main__":
    main()
