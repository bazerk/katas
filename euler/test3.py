import unittest
from problem3 import euler_problem3


class Promblem3Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Basics(self):
        self.assertEqual(euler_problem3(100), 5)
        self.assertEqual(euler_problem3(1000), 5)
        self.assertEqual(euler_problem3(13195), 29)


if __name__ == '__main__':
    unittest.main()
