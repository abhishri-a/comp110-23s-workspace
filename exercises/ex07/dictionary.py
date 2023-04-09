"""Dictionary Functions!"""

__author__ = "730554082"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Switches values and keys for given dictionary."""
    new: dict[str, str] = {}
    for key in original:
        for j in new:
            if original[key] == j:
                raise KeyError("You cannot have multiple Keys that are the same")
        value = original[key]
        new[value] = key
    return new


def favorite_color(dictionary: dict[str, str]) -> str:
    """Gives most mentioned color from a given list."""
    appears_most = ""
    highest_count = 0
    for i in dictionary:
        count = 0
        for j in dictionary:
            if dictionary[i] == dictionary[j]:
                count += 1
        if count > highest_count and count != highest_count:
            highest_count = count
            appears_most = dictionary[i]
            print(f"{count} + {appears_most} + {highest_count}")  
    return appears_most


def count(given: list[str]) -> dict[str, int]:
    """Gives the counnts of an item from a list."""
    new: dict[str, int] = {}
    for i in range(0, len(given)):
        if given[i] in new:
            new[given[i]] += 1
        else:
            new[given[i]] = 1    
    return new