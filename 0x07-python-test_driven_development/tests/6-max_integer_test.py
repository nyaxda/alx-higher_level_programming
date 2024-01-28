#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Test cases for max_integer function"""
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 9, 3, 5, 4]), 9)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([5, 1, 7, 3, 4]), 7)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([1, 3, 2, 4, 5]), 5)
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 5, 2, 3, 4]), 5)
        self.assertEqual(max_integer([1, 5, 3, 2, 4]), 5)
        self.assertEqual(max_integer([5, 3, 2, 1, 4]), 5)
        self.assertEqual(max_integer([5, 4, 12, 4, 1]), 12)
        self.assertEqual(max_integer([5, 3, 4, 2, 1]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([5, 4, 3, 1, 2]), 5)
        self.assertEqual(max_integer([5, 4, 1, 3, 2]), 5)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_non_integer_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])
    
    def test_string(self):
        self.assertEqual(max_integer("string"), 't')
