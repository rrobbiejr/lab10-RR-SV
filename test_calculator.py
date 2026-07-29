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

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    #     fill in code

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(5, 625), 4)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()