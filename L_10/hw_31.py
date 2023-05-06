"""
Написать функцию, которая возвращает слуайную строку заданной длины.
Строка должна состоять из больших и маленьких латинских букв и цифр.
(снижать за это оценку не буду, но лучше постараться сделать так, чтобы символы попадали в строку равномерно)


def get_random_string(length: int) -> str:
    pass

Ограничения:
- Не использовать модуль string
- Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
"""

import random


def get_random_string(length: int) -> str:
    # Formally, alphabet not created manually :)
    alphabet = generate_alphabet()

    result = [random.choice(alphabet) for _ in range(length)]
    return "".join(result)


def generate_alphabet() -> str:
    alphabet = []
    for i in range(48, 125):
        if (char := chr(i)).isalnum():
            alphabet.append(char)
    return "".join(alphabet)


def main() -> None:
    print(get_random_string(10))


if __name__ == "__main__":
    main()
