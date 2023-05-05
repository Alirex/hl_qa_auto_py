"""
Есть текстовый файл. Вывести самую длинную строку.

Функции max, readlines не использовать. Файл может быть большим.
"""
import logging
import pathlib
from dataclasses import dataclass
from typing import Final

from faker import Faker

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FILES_DIR: Final[pathlib.Path] = ROOT_DIR / "files_temp"


@dataclass
class ResultLine:
    content: str = ""
    line_number: int | None = None

    def __str__(self) -> str:
        return (
            f'Line {self.line_number} (len={len(self.content)}): "{self.content!r}"'
            if self.line_number is not None
            else "No lines"
        )


def get_longest_line(file_path: pathlib.Path) -> ResultLine:
    result_line = ResultLine()
    with open(file_path) as file:
        for index, content in enumerate(file, start=1):
            if len(content) > len(result_line.content):
                result_line.content = content
                result_line.line_number = index
    return result_line


def generate_file_if_not_exist(
    file_path: pathlib.Path, amount_of_lines: int = 1_000
) -> None:
    logger = logging.getLogger(__name__)

    if file_path.exists():
        logger.info(f"File already exists: {file_path.as_uri()}")
        return

    fake = Faker()
    logger.info(f"Start creating file: {file_path.as_uri()}")
    with open(file_path, mode="w") as file:
        for _ in range(amount_of_lines):
            file.write(f"{fake.paragraph()}\n")

    logger.info(f"File created: {file_path.as_uri()}")


def main() -> None:
    file_path = FILES_DIR / "hw_20.txt"

    generate_file_if_not_exist(file_path=file_path)

    print(get_longest_line(file_path=file_path))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
