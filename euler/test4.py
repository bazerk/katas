import unittest
from problem4 import check_number_is_palindrome


class Promblem4Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_number_is_palindrome(self):
        self.assertEqual(check_number_is_palindrome(101), True)
        self.assertEqual(check_number_is_palindrome(100), False)
        self.assertEqual(check_number_is_palindrome(131195), False)
        self.assertEqual(check_number_is_palindrome(1234321), True)
        self.assertEqual(check_number_is_palindrome(123321), True)


if __name__ == '__main__':
    unittest.main()
