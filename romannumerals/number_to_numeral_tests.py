import unittest
from roman import number_to_numeral_iterative, number_to_numeral_rec

test_funcs = [number_to_numeral_iterative, number_to_numeral_rec]


class RomanTests(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_Basics(self):
        for number_to_numeral in test_funcs:
            self.assertEqual(number_to_numeral(1), 'I')
            self.assertEqual(number_to_numeral(5), 'V')
            self.assertEqual(number_to_numeral(10), 'X')
            self.assertEqual(number_to_numeral(50), 'L')
            self.assertEqual(number_to_numeral(100), 'C')
            self.assertEqual(number_to_numeral(500), 'D')
            self.assertEqual(number_to_numeral(1000), 'M')

    def test_Advanced(self):
        for number_to_numeral in test_funcs:
            self.assertEqual(number_to_numeral(2), 'II')
            self.assertEqual(number_to_numeral(3), 'III')
            self.assertEqual(number_to_numeral(4), 'IV')
            self.assertEqual(number_to_numeral(6), 'VI')
            self.assertEqual(number_to_numeral(9), 'IX')
            self.assertEqual(number_to_numeral(11), 'XI')
            self.assertEqual(number_to_numeral(12), 'XII')
            self.assertEqual(number_to_numeral(15), 'XV')
            self.assertEqual(number_to_numeral(19), 'XIX')
            self.assertEqual(number_to_numeral(39), 'XXXIX')
            self.assertEqual(number_to_numeral(49), 'XLIX')
            self.assertEqual(number_to_numeral(999), 'CMXCIX')
            self.assertEqual(number_to_numeral(3000), 'MMM')
            self.assertEqual(number_to_numeral(2437), 'MMCDXXXVII')
            self.assertEqual(number_to_numeral(3503), 'MMMDIII')
            self.assertEqual(number_to_numeral(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
