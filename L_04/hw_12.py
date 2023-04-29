"""
В программе есть строка s.

Вывести заголовком строку, котрая состоит из слов, в которых буква 'a' встречается два раза.


s = "aab qq c badcc a qqqqqaqqqqaa tpara"
Aab Tpara
"""


def get_words_with_two_a(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split() if word.count("a") == 2)


def main() -> None:
    s = "aab qq c badcc a qqqqqaqqqqaa tpara"
    print(get_words_with_two_a(s))


if __name__ == "__main__":
    main()
