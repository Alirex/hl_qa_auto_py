"""
В программе есть строка multi_string. Строка состоит из предложений.
Предложение - это набор символов, ограниченных точками или началом строки и точкой.

Записать в список количество слов в каждом предложении.
Слово - набор символов между двумя пробелами или началом строки и пробелом.

Регулярные выражения не использовать.



multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
words_number -> [2, 5, 2]
"""


def count_words_in_sentences(
    multi_string: str,
    #
    sentence_separator: str = ".",
    word_separator: str = " ",
) -> list[int]:
    sentences = multi_string.split(sentence_separator)

    words_number = []
    for sentence in sentences:
        if words := list(filter(bool, sentence.split(word_separator))):
            words_number.append(len(words))
    return words_number


def main() -> None:
    multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
    words_number = count_words_in_sentences(multi_string)
    print(words_number)


if __name__ == "__main__":
    main()
