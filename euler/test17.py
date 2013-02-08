import unittest
from problem17 import number_to_english


class Euler17Tests(unittest.TestCase):

    def test_BasicOutput(self):
        self.assertEqual(number_to_english(1), 'one')
        self.assertEqual(number_to_english(2), 'two')
        self.assertEqual(number_to_english(11), 'eleven')

    def test_LessThanAHundred(self):
        self.assertEqual(number_to_english(20), 'twenty')
        self.assertEqual(number_to_english(21), 'twenty-one')
        self.assertEqual(number_to_english(54), 'fifty-four')
        self.assertEqual(number_to_english(30), 'thirty')
        self.assertEqual(number_to_english(99), 'ninety-nine')

    def test_LessThanAThousand(self):
        self.assertEqual(number_to_english(100), 'one-hundred')
        self.assertEqual(number_to_english(111), 'one-hundred and eleven')
        self.assertEqual(number_to_english(250), 'two-hundred and fifty')
        self.assertEqual(number_to_english(567), 'five-hundred and sixty-seven')

    def test_OneThousand(self):
        self.assertEqual(number_to_english(1000), 'one-thousand')

if __name__ == "__main__":
    unittest.main()
