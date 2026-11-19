
import unittest
from app import add, subtract, multiply

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtraction(self):
        self.assertEqual(subtract(20, 10), 10)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 4), 20)

if __name__ == "__main__":
    unittest.main()
