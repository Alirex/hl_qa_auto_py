"""
Вывести максимальное из трех введенных чисел

Встроенные функции не используем. Только инструкции управления потоком (ифы, циклы)
"""


def get_max(*numbers) -> int:
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def get_numbers(amount: int = 3) -> list[int]:
    return [int(input(f"Enter number {i + 1}: ")) for i in range(amount)]


def main() -> None:
    numbers = get_numbers()
    print(get_max(*numbers))


if __name__ == "__main__":
    main()
