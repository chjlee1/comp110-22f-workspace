"""Test for the util function."""

__author__: str = "730571111"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests only_evens() function with empty list, should return empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Tests only_evens() function with many items."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_many_items_again() -> None:
    """Tests only_evens() function with many items, only one even."""
    xs: list[int] = [1, 3, 5, 7, 9, 10]
    assert only_evens(xs) == [10]


def test_concat_empty() -> None:
    """Tests concat() function with empty lists, should return empty list."""
    xs: list[int] = []
    nums: list[int] = []
    assert concat(xs, nums) == []


def test_concat_many_items() -> None:
    """Tests concat() function with many items."""
    xs: list[int] = [1, 2, 3]
    nums: list[int] = [4, 5, 6]
    assert concat(xs, nums) == [1, 2, 3, 4, 5, 6]


def test_concat_one_empty() -> None:
    """Tests concat() function with one full list and one empty list."""
    xs: list[int] = []
    nums: list[int] = [6, 19, 4, 8]
    assert concat(xs, nums) == [6, 19, 4, 8]


def test_sub_out_of_bounds() -> None:
    """Tests sub() function with full list but with start index greater than end index, should return empty list."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 3, 2) == []


def test_sub_negative_and_over() -> None:
    """Tests sub() function with full list with negative start value and end index greater than list length, should return full list."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, -2, 6) == [10, 20, 30, 40]


def test_sub_many_items() -> None:
    """Tests sub() function with full list with valid start and end values."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]