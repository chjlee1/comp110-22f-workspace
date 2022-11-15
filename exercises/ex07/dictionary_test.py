"""Tests for dictionary.py."""

__author__: str = "730571111"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests invert function with an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_double_keys() -> None:
    """Tests invert function with a dictionary that will invert to two identical keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'Christian': 'Lee', 'Bruce': 'Lee'}
        invert(my_dictionary)


def test_invert_many_items() -> None:
    """Tests invert function with dictionary with many items."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c', 'w': 'd'}


def test_favorite_color_empty() -> None:
    """Tests favorite color function with an empty dictionary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ''


def test_favorite_color_tie() -> None:
    """Tests favorite color function with a dictionary that creates a tie between colors."""
    xs: dict[str, str] = {'Aidan': 'red', 'Michael': 'blue', 'Christian': 'blue', 'Abhinav': 'red'}
    assert favorite_color(xs) == 'red'


def test_favorite_color_many_items() -> None:
    """Tests favorite color function with a dictionary with many items."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Chris": "greed"}
    assert favorite_color(xs) == 'blue'


def test_count_empty() -> None:
    """Tests count function with an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_many_items() -> None:
    """Tests count function with a list with many items."""
    xs: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'e']
    assert count(xs) == {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'e': 2, 'f': 1}


def test_count_many_items_again() -> None:
    """Tests count function with a list with many repeating items."""
    xs: list[str] = ['a', 'b', 'a', 'c', 'a', 'c', 'a', 'c', 'a', 'd']
    assert count(xs) == {'a': 5, 'b': 1, 'c': 3, 'd': 1}