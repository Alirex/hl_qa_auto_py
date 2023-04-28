"""
Запросить у пользователя два целых числа.

Вывести на одной строке выражение их суммы, на второй выражение для произведения:

Enter a: 3
Enter b: 5
3 + 5 = 8
3 * 5 = 15
"""


def print_by_f_strings(a: int, b: int) -> None:
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")


def print_by_separators(a: int, b: int) -> None:
    print(a, "+", b, "=", a + b, sep=" ")
    print(a, "*", b, "=", a * b, sep=" ")


def main() -> None:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print_by_f_strings(a, b)
    print_by_separators(a, b)


if __name__ == "__main__":
    main()
