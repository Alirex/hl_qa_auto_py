"""
hw_28.md
"""
import re
from typing import Final

END_OF_SENTENCE_CHARS: Final[str] = ".?!"
END_OF_SENTENCE_CHARS__ESCAPED: Final[str] = re.escape(END_OF_SENTENCE_CHARS)
WORD_CHARS: Final[str] = "A-Za-z"
pattern = re.compile(
    "(?P<sentence>"
    #
    # First word of sentence.
    "(?P<first_word>"
    "[A-Z]"  # Sentence starts with capital letter.
    f"[{WORD_CHARS}]*"  # Words contains only letters.
    ")"
    #
    f"[{WORD_CHARS}, ]*"  # Sentence contains words, comma (,), and whitespaces.
    f"[{END_OF_SENTENCE_CHARS__ESCAPED}]"  # Sentence ends with "end chars".
    ")"
)


def generate_sentence(text: str, end_of_result_sentence: str = ".") -> str:
    parts = [match.group("first_word") for match in pattern.finditer(text)]
    return (" ".join(parts) + end_of_result_sentence).capitalize()


def main() -> None:
    text = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""

    message = generate_sentence(text)
    print(message)

    # noinspection Assert
    assert message == "Happy wish please goodbye."


if __name__ == "__main__":
    main()
