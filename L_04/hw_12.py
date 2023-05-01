"""
В программе есть строка s.

Вывести заголовком строку, котрая состоит из слов, в которых буква 'a' встречается два раза.


s = "aab qq c badcc a qqqqqaqqqqaa tpara"
Aab Tpara
"""


def get_words_with_two_a__capitalize_by_word(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split() if word.count("a") == 2)


# Better to use this
def get_words_with_two_a__title_all(text: str) -> str:
    return " ".join(word for word in text.split() if word.count("a") == 2).title()


def main() -> None:
    s = "aab qq c badcc a qqqqqaqqqqaa tpara"
    print(get_words_with_two_a__capitalize_by_word(s))
    print(get_words_with_two_a__title_all(s))


if __name__ == "__main__":
    main()
