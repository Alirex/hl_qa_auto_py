"""
Пользователь вводит адрес элемктронной почты. Вывести True, если строка является валидным адресом, иначе False.

Валидным адресом считаем, строку

- в которой встречается один раз '@' и один раз '.'

- '@' идет до '.'

- строка не начинается с '@' и не заканчивается '.'

В комментариях к коду должны быть указаны строки, которыми протестировали код

Регулярные выражения не использовать.


email = "aaa@bbb.ccc"  # True
"""


def is_valid_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    elif email.count(".") != 1:
        return False
    elif email.startswith("@") or email.endswith("."):
        return False
    else:
        index_at = email.index("@")
        index_dot = email.index(".")
        # Handle special case. "." just behind the "@" . "a@.c"
        if index_dot - index_at < 2:
            return False

    return True


def main() -> None:
    data = [
        # Valid
        ("aaa@bbb.ccc", True),
        # Two "@"
        ("aaa@@bbb.ccc", False),
        # Without "@"
        ("aaabbb.ccc", False),
        # Two "."
        ("aaa@bbb..ccc", False),
        # Without "."
        ("aaa@bbb", False),
        # "." before "@"
        ("aaa.bbb@ccc", False),
        # Start with "@"
        ("@aaa.bbb", False),
        # End with "."
        ("aaa@bbb.", False),
        # Special case!!! Valid by task description, but not valid by real life.
        ("aaa@.ccc", False),
    ]

    for email, expected in data:
        result = is_valid_email(email)
        print(f"is_valid_email({email}) == {result}")
        # noinspection Assert
        assert result == expected, f"is_valid_email({email}) == {result} != {expected}"


if __name__ == "__main__":
    main()
