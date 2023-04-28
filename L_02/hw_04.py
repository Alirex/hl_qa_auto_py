"""
Запросить у пользователя два целых числа.

Вывести на одной строке выражение их суммы, на второй выражение для произведения:

Enter a: 3
Enter b: 5
3 + 5 = 8
3 * 5 = 15
"""


def main() -> None:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")


if __name__ == "__main__":
    main()
