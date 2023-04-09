def zip (list1: list[str], list2: list[int]) -> dict[str,int]:
    """creates a dictionary with two lists."""
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return {}
    dictionary: dict[list[str],list[int]] = {}
    for i in range (0,len(list1)):
        dictionary[list1[i]] = list2[i]
    return dictionary
