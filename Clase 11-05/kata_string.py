import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("5"), 5)
    
    def test_two_numbers_returns_sum(self):
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("10,20"), 30)
    
    def test_multiple_numbers_returns_sum(self):
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("1,2,3,4,5"), 15)


if __name__ == "__main__":
    unittest.main()
