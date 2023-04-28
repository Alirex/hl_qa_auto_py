"""
Вывести треугольник, по введенной стороне

> Enter size of triangle: 5
    *
   **
  ***
 ****
*****
"""


def print_triangle_by_end(size: int) -> None:
    for i in range(1, size + 1):
        print(" " * (size - i), end="")
        print("*" * i)


def print_triangle_by_f_string(size: int) -> None:
    for i in range(1, size + 1):
        print(f"{' ' * (size - i)}{'*' * i}")


def print_triangle_by_placeholder(size: int) -> None:
    for i in range(1, size + 1):
        # https://docs.python.org/3/library/string.html#format-specification-mini-language
        # '>' Forces the field to be right-aligned within the available space.
        print(f"{'*' * i:>{size}}")


def main() -> None:
    size = int(input("Enter size of triangle: "))
    print_triangle_by_end(size)
    print_triangle_by_f_string(size)
    print_triangle_by_placeholder(size)


if __name__ == "__main__":
    main()
