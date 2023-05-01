from collections.abc import Callable

import pytest

from L_04.hw_12 import (
    get_words_with_two_a__capitalize_by_word,
    get_words_with_two_a__title_all,
)


@pytest.mark.parametrize(
    "action,",
    (
        get_words_with_two_a__capitalize_by_word,
        get_words_with_two_a__title_all,
    ),
)
def test_benchmark__get_words__simple(action: Callable, benchmark: Callable) -> None:
    benchmark(action, "aab qq c badcc a qqqqqaqqqqaa tpara")


@pytest.mark.parametrize(
    "action,",
    (
        get_words_with_two_a__capitalize_by_word,
        get_words_with_two_a__title_all,
    ),
)
def test_benchmark__get_words__bigger_values(
    action: Callable, benchmark: Callable
) -> None:
    benchmark(action, "aab qq c badcc a qqqqqaqqqqaa tpara" * 1000)
