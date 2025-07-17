import unittest

def sum(a, b):
    return a + b

class TestSumFunction(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(sum(2, 3), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(sum(-2, -3), -5)
    
    def test_mixed_numbers(self):
        self.assertEqual(sum(-2, 3), 1)
    
    def test_large_numbers(self):
        self.assertEqual(sum(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000