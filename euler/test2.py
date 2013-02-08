import unittest
from problem2 import fibbonaci, euler_problem2


class FibbonaciTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Basics(self):
        self.assertEqual(list(fibbonaci(5)), [1, 2, 3])
        self.assertEqual(list(fibbonaci(10)), [1, 2, 3, 5, 8])


class SumEvenFibbonaciTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Basics(self):
        self.assertEqual(euler_problem2(5), 2)
        self.assertEqual(euler_problem2(10), 10)


if __name__ == '__main__':
    unittest.main()
