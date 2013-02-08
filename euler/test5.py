import unittest
from problem5 import euler_problem5


class Promblem4Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_number_is_palindrome(self):
        self.assertEqual(euler_problem5(range(1, 11)), 2520)

if __name__ == '__main__':
    unittest.main()
