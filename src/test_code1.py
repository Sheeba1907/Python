def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("No division by zero")
    else:
        return a/b
    
import unittest
class test(unittest.TestCase):
    def test_divide_valid(self):
        self.assertEqual(divide(10, 0),2)
    def test_raise_error(self):
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()