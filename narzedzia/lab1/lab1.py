def get_divisors(n):
    """Find prime factorization of number n >= 2

    Args:
        n (int): number to factorize

    Returns:
        list: list of prime numbers in ascending order such that product of all of them equals n
    """
    divisors = []
    for i in range(2, n + 1):
        while (n % i == 0):
            divisors.append(i)
            n = n // i
    return divisors

def product_string(factors):
    return '*'.join(str(f) for f in factors)

def factorization_string(n):
    """
    Args:
        n (int): number to factorize

    Returns:
        string: string which represents prime factorization
    """
    return str(n) + ' = ' + product_string(get_divisors(n))

def factorize():
    """Takes a number from standard input and prints its prime factorization to standard output
    """
    n = int(input("Factorizer Pro (TM).\nEnter the number for factorization: "))
    print(factorization_string(n))

import unittest

class TestGetDivisorsFunction(unittest.TestCase):
    def test_factorize_prime(self):
        self.assertEqual(get_divisors(17), [17])

    def test_factorize_composite(self):
        self.assertEqual(get_divisors(12), [2, 2, 3])

    def test_factorize_power_of_prime(self):
        self.assertEqual(get_divisors(8), [2, 2, 2])

    def test_factorize_large_number(self):
        self.assertEqual(get_divisors(120), [2, 2, 2, 3, 5])

    def test_factorize_prime_power(self):
        self.assertEqual(get_divisors(125), [5, 5, 5])

    def test_factorize_one(self):
        self.assertEqual(get_divisors(1), [])


class TestProductStringFunction(unittest.TestCase):
    def test_product_string_empty_list(self):
        self.assertEqual(product_string([]), "")

    def test_product_string_single_factor(self):
        self.assertEqual(product_string([5]), "5")

    def test_product_string_two_factors(self):
        self.assertEqual(product_string([2, 3]), "2*3")

    def test_product_string_multiple_factors(self):
        self.assertEqual(product_string([2, 2, 3, 5]), "2*2*3*5")

    def test_product_string_large_factors(self):
        self.assertEqual(product_string([11, 13, 17]), "11*13*17")

    def test_product_string_mixed_factors(self):
        self.assertEqual(product_string([2, 3, 2, 5, 7]), "2*3*2*5*7")

class TestFactorizeFunction(unittest.TestCase):
    def test_factorize_prime(self):
        self.assertEqual(factorization_string(17), "17 = 17")

    def test_factorize_composite(self):
        self.assertEqual(factorization_string(12), "12 = 2*2*3")

    def test_factorize_power_of_prime(self):
        self.assertEqual(factorization_string(8), "8 = 2*2*2")

    def test_factorize_large_number(self):
        self.assertEqual(factorization_string(120), "120 = 2*2*2*3*5")

    def test_factorize_prime_power(self):
        self.assertEqual(factorization_string(125), "125 = 5*5*5")


if __name__ == '__main__':
    # unittest.main()
    factorize()



            
        
    