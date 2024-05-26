import numpy as np

def which_grow2times(data):
    
    res = []
    m, n = data.shape

    for i in range(m):
        mins = np.minimum.accumulate(data[i,])
        for j in range(n - 1, 0, -1):
            if 2 * mins[j-1] <= data[i, j]:
                res.append(i)
                break
    
    return res

import unittest

class TestWhichGrow2Times(unittest.TestCase):

    def test_single_row_with_condition(self):
        data = np.array([[0.7, 0.5, 0.6, 1.1]])
        expected = [0]
        result = which_grow2times(data)
        self.assertEqual(result, expected)
    
    def test_single_row_without_condition(self):
        data = np.array([[0.7, 0.8, 0.9, 1.0]])
        expected = []
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_multiple_rows(self):
        data = np.array([[0.7, 0.5, 0.6, 1.1],
                         [0.2, 0.4, 0.3, 0.9],
                         [1.0, 1.5, 0.5, 0.6]])
        expected = [0, 1]
        result = which_grow2times(data)
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        data = np.array([[]])
        expected = []
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_all_valid_rows(self):
        data = np.array([[0.1, 0.5, 0.6, 1.2],
                         [0.3, 0.2, 0.6, 1.5]])
        expected = [0, 1]
        result = which_grow2times(data)
        self.assertEqual(result, expected)

import unittest
import numpy as np

class TestWhichGrow2TimesAdditional(unittest.TestCase):

    def test_no_elements_in_row(self):
        data = np.array([[], []])
        expected = []
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        data = np.array([[1e10, 2e10, 1.5e10, 3e10],
                         [5e10, 1e11, 2e11, 4e11]])
        expected = [0, 1]
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_all_elements_equal(self):
        data = np.array([[1, 1, 1, 1],
                         [2, 2, 2, 2]])
        expected = []
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_single_column(self):
        data = np.array([[1],
                         [2],
                         [3],
                         [4]])
        expected = []
        result = which_grow2times(data)
        self.assertEqual(result, expected)

    def test_two_columns_with_valid_condition(self):
        data = np.array([[0.5, 1.1],
                         [0.25, 0.5],
                         [1.2, 2.4]])
        expected = [0, 1, 2]
        result = which_grow2times(data)
        self.assertEqual(result, expected)

# if __name__ == '__main__':
#     unittest.main()

outs = np.load("sample_treated.npz")['outputs']
print(which_grow2times(outs))