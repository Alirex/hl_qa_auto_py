from collections.abc import Callable

import pytest

from L_09.hw_29 import (
    linearize_list,
    linearize_list_by_deque,
    get_lst,
    example_lst,
)


@pytest.mark.parametrize(
    "action,",
    (
        linearize_list,
        linearize_list_by_deque,
    ),
)
def test_benchmark__linearize__simple(action: Callable, benchmark: Callable) -> None:
    result = benchmark(action, get_lst())
    assert result == example_lst
