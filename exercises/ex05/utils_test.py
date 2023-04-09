"""Testing out utility functions!"""

__author__ = "730554082"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Edge case with empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_one() -> None:
    """Use case with only odd numbers."""
    odd_list: list[int] = [1, 3, 5, 7]
    assert only_evens(odd_list) == [1, 3, 5, 7]


def test_only_evens_two() -> None:
    """Use case with random numbers."""
    random_list: list[int] = [3, 4, 1, 7, 2, 8, 6]
    assert only_evens(random_list) == [4, 2, 8, 6]


def test_concat() -> None:
    """Edge case with empty list."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []


def test_concat_one() -> None:
    """Use case with only one not empty list."""
    list_a: list[int] = [1, 2, 3, 4]
    list_b: list[int] = []
    assert concat(list_a, list_b) == [1, 2, 3, 4]


def test_concat_two() -> None:
    """Use case with two lists with numbers."""
    list_a: list[int] = [1, 2, 3, 4]
    list_b: list[int] = [3, 5, 9]   
    assert concat(list_a, list_b) == [1, 2, 3, 4, 3, 5, 9]


def test_sub() -> None:
    """Edge case with empty list."""
    list_a: list[int] = []
    start_idx: int = 0
    end_idx: int = 0
    assert sub(list_a, start_idx, end_idx) == []


def test_sub_one() -> None:
    """Use case with same start and end index."""
    list_a: list[int] = [2, 3, 4, 9]
    start_idx: int = 2
    end_idx: int = 2
    assert sub(list_a, start_idx, end_idx) == []


def test_sub_two() -> None:
    """Use case with a filled list and different start and end indexes."""
    list_a: list[int] = [2, 3, 4, 9, 8]
    start_idx: int = 1
    end_idx: int = 3
    assert sub(list_a, start_idx, end_idx) == [3, 4, 9]