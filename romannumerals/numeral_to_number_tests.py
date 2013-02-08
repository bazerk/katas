import unittest
from roman import numeral_to_number


class RomanTests(unittest.TestCase):

    def test_Basics(self):
        self.assertEqual(numeral_to_number('I'), 1)
        self.assertEqual(numeral_to_number('V'), 5)
        self.assertEqual(numeral_to_number('X'), 10)
        self.assertEqual(numeral_to_number('L'), 50)
        self.assertEqual(numeral_to_number('C'), 100)
        self.assertEqual(numeral_to_number('D'), 500)
        self.assertEqual(numeral_to_number('M'), 1000)

    def test_Advanced(self):
        self.assertEqual(numeral_to_number('II'), 2)
        self.assertEqual(numeral_to_number('III'), 3)
        self.assertEqual(numeral_to_number('IV'), 4)
        self.assertEqual(numeral_to_number('VI'), 6)
        self.assertEqual(numeral_to_number('IX'), 9)
        self.assertEqual(numeral_to_number('XI'), 11)
        self.assertEqual(numeral_to_number('XII'), 12)
        self.assertEqual(numeral_to_number('XV'), 15)
        self.assertEqual(numeral_to_number('XIX'), 19)
        self.assertEqual(numeral_to_number('XXXIX'), 39)
        self.assertEqual(numeral_to_number('XLIX'), 49)
        self.assertEqual(numeral_to_number('MMM'), 3000)
        self.assertEqual(numeral_to_number('MMMI'), 3001)
        self.assertEqual(numeral_to_number('CMXCIX'), 999)
        self.assertEqual(numeral_to_number('MMCDXXXVII'), 2437)
        self.assertEqual(numeral_to_number('MMMDIII'), 3503)
        self.assertEqual(numeral_to_number('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()
