"""
Пользователь вводит строку. Вывести True, если строка является палиндромом, иначе False.

Палиндром - строка, которя читается одинаково слева и справа.

Если в строке есть ведущие или конечные пробелы, они не учитываются.

Проверка должна быть регистронезависимой.

Решить минимум двумя способами.



"    aBC cba " # True
"a BCQcb a    " # True
" ab bca"  # False
"""


def is_palindrome_1(text: str) -> bool:
    text = text.strip().lower()
    return text == text[::-1]


def is_palindrome_2(text: str) -> bool:
    text = text.strip().lower()
    return all(text[i] == text[-i - 1] for i in range(len(text) // 2))


def is_palindrome_3(text: str) -> bool:
    text = text.strip().lower()
    return all(map(lambda i: text[i] == text[-i - 1], range(len(text) // 2)))


# noinspection Assert
def main() -> None:
    data = [
        ("    aBC cba ", True),
        ("a BCQcb a    ", True),
        (" ab bca", False),
    ]

    actions = [
        is_palindrome_1,
        is_palindrome_2,
        is_palindrome_3,
    ]

    for text, expected in data:
        for action in actions:
            result = action(text)
            print(f"{action.__name__}({text}) == {result}")
            assert (
                result == expected
            ), f"{action.__name__}({text}) == {result} != {expected}"


if __name__ == "__main__":
    main()
