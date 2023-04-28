"""
Пользователь вводит высоту и ширину прямоугольника (целые числа) и символ.

Вывести прямоугольник составленный из введенного символа заданного размера

> Enter height of rectangular: 3
> Enter width of rectangular: 6
> Enter symbol to build rectangular with: ^
^^^^^^
^^^^^^
^^^^^^
"""
from typing import NamedTuple


def build_rectangle(height: int, width: int, symbol: str) -> None:
    for _ in range(height):
        print(symbol * width)


class RectangleConfig(NamedTuple):
    height: int
    width: int
    symbol: str


def get_config() -> RectangleConfig:
    return RectangleConfig(
        height=int(input("Enter height of rectangular: ")),
        width=int(input("Enter width of rectangular: ")),
        symbol=input("Enter symbol to build rectangular with: "),
    )


def main() -> None:
    config = get_config()
    build_rectangle(
        height=config.height,
        width=config.width,
        symbol=config.symbol,
    )


if __name__ == "__main__":
    main()
