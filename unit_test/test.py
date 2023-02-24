import unittest

from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5),120, "factorial of 5 is 120")
        self.assertEqual(factorial(10),3628800, "factorial of 10 is 3628800")
        self.assertEqual(factorial(1),1, "factorial of 1 is 1")

    # def test

if __name__ == '__main__':
    unittest.main()