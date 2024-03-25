def cp(lst):
    """
    Makes a copy of the input list.
    
    Args:
    lst (list): The list to be copied.
    
    Returns:
    list: A new list containing the same elements as the input list.
    """
    res = []
    for e in lst:
        res.append(e)
    return res

def append_greater(lst, el):
    """
    Appends an element to the input list if it is greater than the last element of the list.
    
    Args:
    lst (list): The list to which the element will be appended.
    el: The element to be appended to the list.
    """
    if (lst == [] or el > lst[-1]):
        lst.append(el)


def sorted_set_sum(lst1, lst2):
    """
    Returns the set-theoretic sum of two lists representing sets, with elements in ascending order.
    
    Args:
    lst1 (list): The first list representing a set (sorted in ascending order).
    lst2 (list): The second list representing a set (sorted in ascending order).
    
    Returns:
    list: The set-theoretic sum of lst1 and lst2, represented as a list with elements in ascending order.
    """
    
    # If one list is empty, return copy of the other one
    if (lst1 == []):
        return cp(lst2)
    if (lst2 == []):
        return cp(lst1)

    # Create a list to store the result
    res = []
    # Initialize indices for lst1, lst2
    i, j = 0, 0

    # Iterate until one of the lists is exhausted
    while (True):
        while(lst1[i] <= lst2[j]):
            append_greater(res, lst1[i])
            i += 1
            # If all elements of lst1 have been processed, append remaining elements of lst2 to the result list and return
            if (i == len(lst1)):
                for k in range(j, len(lst2)):
                    append_greater(res, lst2[k])
                return res
        # Swap lst1 and lst2, and their corresponding indices
        lst1, lst2 = lst2, lst1
        i, j = j, i
    
    return res


import unittest

class TestCopyList(unittest.TestCase):
    def test_empty_list(self):
        original = []
        copied = cp(original)
        self.assertEqual(copied, [])

    def test_non_empty_list(self):
        original = [1, 2, 3]
        copied = cp(original)
        self.assertEqual(copied, [1, 2, 3])

    def test_list_with_duplicates(self):
        original = [1, 2, 2, 3, 3, 3]
        copied = cp(original)
        self.assertEqual(copied, [1, 2, 2, 3, 3, 3])


class TestSortedSetSum(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(sorted_set_sum([], []), [])

    def test_identical_lists(self):
        self.assertEqual(sorted_set_sum([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_one_list_empty(self):
        self.assertEqual(sorted_set_sum([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(sorted_set_sum([1, 2, 3], []), [1, 2, 3])

    def test_non_empty_lists(self):
        self.assertEqual(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]), [-3, -2, 0, 1, 3, 34])

    def test_duplicate_elements(self):
        self.assertEqual(sorted_set_sum([1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

    def test_lists_with_negative_elements(self):
        self.assertEqual(sorted_set_sum([-5, -4, -3, -2, -1], [-3, -2, -1, 0, 1]), [-5, -4, -3, -2, -1, 0, 1])

    def test_lists_with_positive_elements(self):
        self.assertEqual(sorted_set_sum([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_one_list_length_one(self):
        self.assertEqual(sorted_set_sum([5], [1, 2, 3]), [1, 2, 3, 5])
        self.assertEqual(sorted_set_sum([1, 2, 3], [5]), [1, 2, 3, 5])
        self.assertEqual(sorted_set_sum([5], []), [5])
        self.assertEqual(sorted_set_sum([], [5]), [5])

    def test_both_lists_length_one(self):
        self.assertEqual(sorted_set_sum([5], [3]), [3, 5])
        self.assertEqual(sorted_set_sum([3], [5]), [3, 5])
        self.assertEqual(sorted_set_sum([5], [5]), [5])


if __name__ == '__main__':
    unittest.main()

    

    
