import numpy as np

arr1 = np.full(10, 100)
arr2 = np.full(10, 156)
assert len(arr1) == 10
assert len(arr2) == 10
assert np.all(arr1 == 100)
assert np.all(arr2 == 156)
arr2 = -arr1
assert np.all(arr1 + arr2 == 0)
