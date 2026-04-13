import unittest
from calculator import *
# https://github.com/your-username/lab11-P-NA
# Partner 1: Priyanshou bhattacharjee
# Partner 2: Not responsive


class TestCalculator(unittest.TestCase):

    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)
    ##########################

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(16, 2), 4)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    ##########################

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

        with self.assertRaises(ValueError):
            square_root(-1)



# Do not touch this
if __name__ == "__main__":
    unittest.main()