"""
Написать декоратор с параметром.
Если применить его к функции, он будет выводить в файл,
который передали параметром, сколько раз вызывалась функция на момент вызова.



@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(4, 6))


data.txt content:
Function 'add' was called 1 times
Function 'add' was called 2 times
"""

import pathlib
from functools import wraps
from typing import ParamSpec, TypeVar
from collections.abc import Callable

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
OriginalFunc = Callable[Param, ReturnType]
DecoratedFunc = Callable[Param, ReturnType]


def call_counter(file_path: str | pathlib.Path):
    file_path = pathlib.Path(file_path)

    def decorator(func: OriginalFunc) -> DecoratedFunc:
        @wraps(func)
        def wrapper(*args, **kwargs) -> ReturnType:
            wrapper.counter += 1
            message = f"Function '{func.__name__}' was called {wrapper.counter} times"

            with open(file_path, mode="a") as f:
                f.write(f"{message}\n")

            return func(*args, **kwargs)

        wrapper.counter = 0
        return wrapper

    return decorator


@call_counter("data.txt")
def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(add(4, 6))
    print(add(4, 6))

    # Check if the name of the function is correct
    print(add.__name__)

    # # Check type hints
    # with contextlib.suppress(TypeError):
    #     print(add(4, 6, 7))


if __name__ == "__main__":
    main()
