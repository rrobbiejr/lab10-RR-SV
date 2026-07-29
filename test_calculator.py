import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(3, 3), 6)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-6, -6), -12)

    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(sub(10, 6), 4)
        self.assertEqual(sub(-3, -3), 0)
        self.assertEqual(sub(0, 5), -5)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10,1), 10)
        self.assertEqual(mul(50, 3), 150)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10,1), .1)
        self.assertEqual(div(2, 4), 2)
        self.assertEqual(div(-2, 10), -5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    #     fill in code

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 8), 8)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(0)
    ########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
