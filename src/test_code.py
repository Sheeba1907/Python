import unittest

def add(a,b):
    return a+b

class test(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(add(4,5), 9)
    def test_all_negative(self):
        self.assertEqual(add(-1, -1), -2)
    def test_all_mixed(self):
        self.assertEqual(add(-1, 5), 4)

if __name__ == "__main__":
    unittest.main()


