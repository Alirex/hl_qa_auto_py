"""
Напишите функцию read_last(file_path, symbol_number),
которая выводить на печать построчно последние symbol_number символов в каждой строке (перевод строки не учитывать).

Пустые строки - пропускать.



def read_last(file_path, symbol_number):
    pass

read_last('read_last.txt', 6)


read_last.txt ->
456789
345678
234567
Line5
"""
import pathlib


def read_last(file_path: pathlib.Path, symbol_number: int) -> None:
    with open(file_path) as f:
        for line in f:
            if not line.strip():
                continue

            message = line.removesuffix("\n")[-symbol_number:]
            print(message)


def main() -> None:
    file_path = pathlib.Path(__file__).parent / "hw_22_data" / "read_last.txt"
    read_last(
        file_path=file_path,
        symbol_number=6,
    )


if __name__ == "__main__":
    main()
