def sublist(lst1,lst2):
    """
    Checks if the first given list is a sublist of the second. The items from lst1 do not have to appear next to each other
    in the lst2 list, but their order must be preserved.

    Args:
        lst1 (list): Potential sublist
        lst2 (list): The list to search within.

    Returns:
        bool: True if lst1 is a sublist of lst2, False otherwise.
    """

    if (lst1 == []):
        return True

    i = 0
    for e in lst2:
        if (lst1[i] == e):
            i += 1
            if (i == len(lst1)):
                return True

    return False

import unittest


class TestSublist(unittest.TestCase):
    def test_empty_lists(self):
        self.assertTrue(sublist([], []))
        self.assertTrue(sublist([], [1, 2, 3]))

    def test_single_item_sublist(self):
        self.assertTrue(sublist([2], [1, 2, 3]))

    def test_ordered_sublist(self):
        self.assertTrue(sublist([1, 3, 4], [1, 2, 3, 4, 5]))

    def test_unordered_sublist(self):
        self.assertFalse(sublist([1, 4, 3], [1, 2, 3, 4, 5]))

    def test_no_match(self):
        self.assertFalse(sublist([6, 7, 8], [1, 2, 3, 4, 5]))

    def test_duplicate_items(self):
        self.assertTrue(sublist([1, 1, 2], [0, 1, 1, 2, 3]))
    
    def test_full_list_match(self):
        self.assertTrue(sublist([1, 2, 3], [1, 2, 3]))

    def test_sublist_at_end(self):
        self.assertTrue(sublist([3, 4, 5], [1, 2, 3, 4, 5]))

    def test_sublist_at_beginning(self):
        self.assertTrue(sublist([1, 2, 3], [1, 2, 3, 4, 5]))

    def test_sublist_in_middle(self):
        self.assertTrue(sublist([2, 3], [1, 2, 3, 4, 5]))

    def test_large_lists(self):
        lst1 = list(range(1000000))
        lst2 = list(range(1000000))
        self.assertTrue(sublist(lst1, lst2))

if __name__ == '__main__':
    unittest.main()
