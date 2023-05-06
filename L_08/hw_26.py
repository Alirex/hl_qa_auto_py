"""
Написать декоратор skip, которым можно декорировать функции.

Если переданное выражение condition истинное, функция не должна выполнятся,
а должна вывестись строка переданная в аргументе reason.

Если выражение condition ложное, функция должна выполнится.

def skip(condition, reason=''):
    pass

Пример использования:

@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()  # Skipped because of JIRA-123 bug
"""
from typing import ParamSpec, TypeVar
from collections.abc import Callable

from functools import wraps

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
OriginalFunc = Callable[Param, ReturnType]
DecoratedFunc = Callable[Param, ReturnType]


def skip(condition: bool, reason: str):
    def decorator(func: OriginalFunc) -> DecoratedFunc:
        @wraps(func)
        def wrapper(*args, **kwargs) -> ReturnType:
            if condition:
                print(reason)
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator


@skip(condition=True, reason="Skipped because of JIRA-123 bug")
def test_two_plus_two():
    # sourcery skip: simplify-numeric-comparison
    # noinspection Assert
    assert 2 + 2 == 5


def main() -> None:
    test_two_plus_two()


if __name__ == "__main__":
    main()
