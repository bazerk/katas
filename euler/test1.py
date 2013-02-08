import unittest
from problem1 import euler_problem1


class Promblem1Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Basics(self):
        self.assertEqual(euler_problem1(4), 3)
        self.assertEqual(euler_problem1(6), 8)
        self.assertEqual(euler_problem1(10), 23)
        self.assertEqual(euler_problem1(1), 0)
        self.assertEqual(euler_problem1(1000), 233168)


if __name__ == '__main__':
    unittest.main()
