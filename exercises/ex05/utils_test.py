"""Testing out utility functions"""

__author__ = "730554082"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """edge case with empty list"""
    assert only_evens([]) == []

def test_only_evens_one() -> None:
    """use case with only odd numbers"""
    odd_list = [1,3,5,7]
    assert only_evens([odd_list]) == odd_list

def test_only_evens_two() -> None:
    """use case with random numbers"""
    random_list = [3,4,1,7,2,8,6]
    assert only_evens([random_list]) == [4,2,8,6]

def test_concat() -> None:
    """edge case with empty list"""
    assert concat([]) == []

def test_concat_one() -> None:
    """use case with only one not empty list"""
    assert concat([3,5,9],[]) == [3,5,9]

def test_concat_two() -> None:
    """use case with two lists with numbers"""
    assert concat([2,4],[1,9]) == [2,4,1,9]

def test_sub() -> None:
    """edge case with empty list"""
    assert sub([]) == []

def test_sub_one() -> None:
    """use case with same start and end index"""
    assert sub([1,3,4],1,1) == []

def test_sub_one() -> None:
    """use case with a filled list and different start and end indexes"""
    assert sub([4,9,2,3,1],2,4) == [2,3]