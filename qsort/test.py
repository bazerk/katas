import unittest
from qsort import qsort, qsort2


class QsortSortTests(unittest.TestCase):

    def test_Basics(self):
        self.assertEqual(qsort([1,2,3]), [1,2,3])
        self.assertEqual(qsort([3,2,1]), [1,2,3])
        self.assertEqual(qsort([1]), [1])
        self.assertEqual(qsort([2,1]), [1,2])
        self.assertEqual(qsort([2,1,6,7,7,2,8,1,99,4,9,16]), [1, 1, 2, 2, 4, 6, 7, 7, 8, 9, 16, 99])



class QsortSort2Tests(unittest.TestCase):

    def test_Basics(self):
        list = [1,2,3]
        qsort2(list)
        self.assertEqual(list, [1,2,3])
        list = [3,2,1]
        qsort2(list)
        self.assertEqual(list, [1,2,3])
        list = [1]
        qsort2(list)
        self.assertEqual(list, [1])
        list = [2,1]
        qsort2(list)
        self.assertEqual(list, [1,2])
        list = [2,1,6,7,7,2,8,1,99,4,9,16]
        qsort2(list)
        self.assertEqual(list, [1, 1, 2, 2, 4, 6, 7, 7, 8, 9, 16, 99])

if __name__ == '__main__':
    unittest.main()