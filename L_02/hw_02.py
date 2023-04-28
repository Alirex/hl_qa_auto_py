"""
Создать список из трех имен котов/собак

Вывести через запятую и пробел:

Murzik, Barsik, Pantera
"""
from collections.abc import Iterable


def print_by_join(items: Iterable[str]) -> None:
    message = ", ".join(items)
    print(message)


def print_by_separator(items: Iterable[str]) -> None:
    print(*items, sep=", ")


def main() -> None:
    animals = ["Murzik", "Barsik", "Pantera"]

    print_by_join(items=animals)
    print_by_separator(items=animals)


if __name__ == "__main__":
    main()
