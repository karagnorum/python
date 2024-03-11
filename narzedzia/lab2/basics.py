def how_many(lst, what):
    """Finds number of occurences of an element in a list

    Args:
        lst (list): a list to search
        what (Any): element to find

    Returns:
        int: number of occurences
    """
    count = 0
    for e in lst:
        if e == what:
            count += 1 
    return count

def reverse(lst):
    """
    Args:
        lst (list): list to reverse

    Returns:
        list: reversed list
    """
    res = []
    for i in range(len(lst)-1, -1, -1):
        res.append(lst[i])
    return res



