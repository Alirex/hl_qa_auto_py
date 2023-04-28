"""
Пользователь вводит минимальную и максимальную ширину "бриллиантового" паттерна.

Вывести "бриллиант" с заданными размерами составленный из символов '*'

Если введенная минимальная ширина больше максимальной ширины, вывести предупреждение и завершить программу.

Если разность максимальной и минимальной ширины не кратно 2, вывести предупреждение (через print) и завершить программу.

> Enter minimal width: 3
> Enter maximal width: 5
 ***
*   *
 ***
> Enter minimal width: 1
> Enter maximal width: 3
 *
* *
 *
> Enter minimal width: 2
> Enter maximal width: 6
  **
 *  *
*    *
 *  *
  **
> Enter minimal width: 3
> Enter maximal width: 9
   ***
  *   *
 *     *
*       *
 *     *
  *   *
   ***
"""


def build_diamond(
    min_width: int,
    max_width: int,
    #
    tile__line: str = "*",
    tile__background: str = " ",
) -> None:
    if min_width > max_width:
        print("Minimal width is greater than maximal width!")
        return
    if (max_width - min_width) % 2 != 0:
        print("Difference between maximal and minimal width is not even!")
        return

    if min_width == max_width:
        # For square diamond
        full_height = max_width
        width_change = 0
    else:
        half_height = (max_width - min_width) // 2
        full_height = half_height * 2 + 1  # +1 for middle row

        width_change = 2

    width = min_width
    modifier = 1

    for height_level in range(1, full_height + 1):
        # Symmetric padding
        padding = (max_width - width) // 2

        is_full_line = height_level in (1, full_height)

        print(
            tile__background * padding,
            tile__line,
            (tile__line if is_full_line else tile__background) * (width - 2),
            tile__line,
            tile__background * padding,
            sep="",
        )

        if width_change:
            if width == max_width:
                modifier = -1

            width += width_change * modifier


def main() -> None:
    # build_diamond(
    #     min_width=4,
    #     # min_width=10,
    #     max_width=10,
    #     #
    #     tile__line='0',
    #     tile__background='-',
    # )

    min_width = int(input("Enter minimal width: "))
    max_width = int(input("Enter maximal width: "))
    build_diamond(
        min_width=min_width,
        max_width=max_width,
    )


if __name__ == "__main__":
    main()
