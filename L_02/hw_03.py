"""
Создать список из трех стран.

Создать словарь из трех пар ключ-значение.
Ключом должна быть строка с названием страны из первого списка, значением строка со столицей.

Вывести каждую пару на отдельной строке, разделить ключ-значение двоеточием и пробелом:

Ukraine: Kyiv
Spain: Madrid
Italy: Rome
"""


def main() -> None:
    countries = ["Ukraine", "Spain", "Italy"]

    capitals = {
        "Ukraine": "Kyiv",
        "Spain": "Madrid",
        "Italy": "Rome",
    }

    for country in countries:
        print(f"{country}: {capitals[country]}")


if __name__ == "__main__":
    main()
