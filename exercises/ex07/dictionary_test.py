"""Testing our dictionary functions."""

__author__ = "730554082"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Edge case with empty dict."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Use case with 4 keys and values."""
    x: dict[str, str] = {"one": "a", "two": "b", "three": "c", "four": "d"}
    assert invert(x) == {"a": "one", "b": "two", "c": "three", "d": "four"}


def test_invert_two() -> None:
    """Use case where keys and values are the same."""
    x: dict[str, str] = {"one": "one", "two": "two", "three": "three", "four": "four"}
    assert invert(x) == {"one": "one", "two": "two", "three": "three", "four": "four"}


def test_favorite_color() -> None:
    """Edge case with empty dict."""
    x: dict[str, str] = {}
    assert favorite_color(x) == ("")


def test_favorite_color_one() -> None:
    """Use case with 4 keys and values."""
    x: dict[str, str] = {"becky": "yellow", "nora": "white", "bob": "green", "andy": "white"}
    assert favorite_color(x) == ("white")


def test_favorite_color_two() -> None:
    """Use case with 2 colors mentioned the same amount of times."""
    x: dict[str, str] = {"becky": "white", "nora": "white", "bob": "yellow", "andy": "green", "mike": "yellow"}
    assert favorite_color(x) == ("white")


def test_count() -> None:
    """Edge case with empty list."""
    x: list[str] = ()
    assert count(x) == ()


def test_count_one() -> None:
    """Use case with 3 items."""
    x: list[str] = ["a", "b", "c", "a", "a", "b"]
    assert count(x) == {"a": 3, "b": 2, "c": 1}


def test_count_two() -> None:
    """Use case with one item repeated 6 times."""
    x: list[str] = ["a", "a", "a", "a", "a", "a"]
    assert count(x) == {"a": 6}