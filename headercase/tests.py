import unittest
from headercase import convert


class HeadcaseTests(unittest.TestCase):

    def test_RunTestCases(self):
        test_cases = [
            ("CamelCase", "Camel Case"),
            ("Sentance case", "Sentance Case"),
            ("header", "Header"),
            ("headerTime", "Header Time"),
            ("TestDNA", "Test DNA"),
            ("BBC", "BBC"),
            ("Testing123", "Testing 123"),
            ("DNATestCases", "DNA Test Cases"),
            ("123123", "123123"),
            ("Bam!InYoFace", "Bam! In Yo Face"),
            ("123Tests", "123 Tests"),
            ("What_about_this", "What About This")
        ]

        for test in test_cases:
            self.assertEqual(test[1], convert(test[0]))


if __name__ == '__main__':
    unittest.main()
