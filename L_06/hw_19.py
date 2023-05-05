"""
Выборка из списка словарей

Есть список состоящий из словарей. Каждый словарь описывает пользователся и имеет два ключа: 'name' (str) и 'age' (int).

Создать и вывести список имен пользователей чей возраст от 18 лет (включительно).


users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

['Olaf Andvarafors', 'Brun Du Barnstokr']
"""
from typing import TypedDict, TypeAlias

T_NAME: TypeAlias = str
T_AGE: TypeAlias = int


class UserAsDict(TypedDict):
    name: T_NAME
    age: T_AGE


def get_users_older_than_and_including(
    users: list[UserAsDict], age: T_AGE = 18
) -> list[T_NAME]:
    return [user["name"] for user in users if user["age"] >= age]


def main() -> None:
    users = [
        {"name": "Luarvik L. Luarvik", "age": 17},
        {"name": "Olaf Andvarafors", "age": 18},
        {"name": "Brun Du Barnstokr", "age": 19},
    ]

    print(get_users_older_than_and_including(users=users))


if __name__ == "__main__":
    main()
