import unittest
import euler


class EulerTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_number_is_palindrome(self):
        self.assertEqual(euler.test_prime(2), True)
        self.assertEqual(euler.test_prime(3), True)
        self.assertEqual(euler.test_prime(4), False)
        self.assertEqual(euler.test_prime(5), True)
        self.assertEqual(euler.test_prime(6), False)
        self.assertEqual(euler.test_prime(7), True)

    def test_total_primes(self):
        self.assertEqual(euler.total_primes(1), [2])
        self.assertEqual(euler.total_primes(2), [2, 3])
        self.assertEqual(euler.total_primes(3), [2, 3, 5])
        self.assertEqual(euler.total_primes(6), [2, 3, 5, 7, 11, 13])

    def test_erasthonens(self):
        self.assertEqual(euler.generate_primes_by_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(euler.generate_primes_by_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_divisors(self):
        self.assertEqual(euler.count_divisors(28), 6)
        #self.assertEqual(euler.count_divisors(1), 1)
        self.assertEqual(euler.count_divisors(2), 2)
        self.assertEqual(euler.count_divisors(3), 2)
        self.assertEqual(euler.count_divisors(10), 4)

    def test_generate_triangle_numbers(self):
        generated = []
        for i in euler.generate_triangle_numbers():
            generated.append(i)
            if len(generated) == 7:
                break
        self.assertEqual(generated, [1, 3, 6, 10, 15, 21, 28])

    def test_vector_addition(self):
        v1 = euler.Vector(1, 1)
        v2 = euler.Vector(2, 1)
        self.assertEqual(v1 + v2, euler.Vector(3, 2))

    def test_max_triangle_traverse(self):
        self.assertEqual(23, euler.traverse_triangle_max_sum([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))

    def test_is_leap_year(self):
        self.assertEqual(euler.is_leap_year(1900), False)
        self.assertEqual(euler.is_leap_year(1904), True)
        self.assertEqual(euler.is_leap_year(2000), True)
        self.assertEqual(euler.is_leap_year(2001), False)

if __name__ == '__main__':
    unittest.main()
