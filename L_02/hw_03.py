"""
Создать список из трех стран.

Создать словарь из трех пар ключ-значение.
Ключом должна быть строка с названием страны из первого списка, значением строка со столицей.

Вывести каждую пару на отдельной строке, разделить ключ-значение двоеточием и пробелом:

Ukraine: Kyiv
Spain: Madrid
Italy: Rome
"""


def print_by_separators(countries: list, capitals: dict) -> None:
    for country in countries:
        print(country, capitals[country], sep=": ")


def print_by_f_strings(countries: list, capitals: dict) -> None:
    for country in countries:
        print(f"{country}: {capitals[country]}")


def main() -> None:
    countries = ["Ukraine", "Spain", "Italy"]

    capitals = {
        "Ukraine": "Kyiv",
        "Spain": "Madrid",
        "Italy": "Rome",
    }

    print_by_separators(countries, capitals)
    print_by_f_strings(countries, capitals)


if __name__ == "__main__":
    main()
