#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """test for Square class"""
    def test_normal_cases(self):
        """normal test cases"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)

        """resetting"""
        Base.reset_nb_objects()

    def test_exceptions(self):
        """testing for exceptions"""
        with self.assertRaises(ValueError):
            s1 = Square(-5, 10)
        with self.assertRaises(TypeError):
            s2 = Square("5", 10)
        with self.assertRaises(ValueError):
            s3 = Square(5, -10)
        with self.assertRaises(TypeError):
            s4 = Square(5, "10")
        with self.assertRaises(ValueError):
            s5 = Square(5, 10, -1)
        with self.assertRaises(TypeError):
            s6 = Square(5, 10, "1")
        with self.assertRaises(ValueError):
            s7 = Square(5, 10, -1, 1)
        with self.assertRaises(TypeError):
            s8 = Square(5, 10, "1", 5)
        with self.assertRaises(TypeError):
            s9 = Square()
        with self.assertRaises(TypeError):
            s10 = Square(20, 10, 5, 2, 3, 7)

        """resetting"""
        Base.reset_nb_objects()

    def test_display(self):
        s1 = Square(4)
        s2 = Square(2, 2)
        s3 = Square(2, 2, 1)

        original_output = sys.stdout

        try:
            #stdout to StringIO object
            sys.stdout = StringIO()
            s1.display()
            output = sys.stdout.getvalue()
            #testing output
            self.assertEqual(output, '####\n' * 4)
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

            s2.display()
            output = sys.stdout.getvalue()
            #testing output
            self.assertEqual(output, '  ##\n' * 2)
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

            s3.display()
            output = sys.stdout.getvalue()
            self.assertEqual(output, '\n' +  '  ##\n' * 2)
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

        finally:
            #restoring stdout to original value
            sys.stdout = original_output

        """resetting"""
        Base.reset_nb_objects()

        def test_str(self):
            s1 = Square(4)
            s2 = Square(2, 2)
            s3 = Square(2, 2, 1)
            s4 = Square(2, 2, 1, 20)

            self.assertEqual(str(s1), "[Square] (1) 0/0 - 4")
            self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
            self.assertEqual(str(s3), "[Square] (3) 2/1 - 2")
            self.assertEqual(str(s4), "[Square] (20) 2/1 - 2")

            """resetting"""
            Base.reset_nb_objects()

        def test_update(self):
            s1 = Square(10, 10, 10, 10)
            s1.update(89)
            self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
            s1.update(89, 2)
            self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
            s1.update(89, 2, 3)
            self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")
            s1.update(89, 2, 3, 4)
            self.assertEqual(str(s1), "[Square] (89) 3/4 - 2/3")

            """resetting"""
            Base.reset_nb_objects()

        def test_square_dict_representation(self):
            s1 = Square(10, 2, 1)
            s1_dictionary = s1.to_dictionary()
            s2 = Square(1, 1)
            s2.update(**s1_dictionary)
            expected_square_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}

            self.assertIsInstance(s1_dictionary, dict)
            self.assertEqual(s1_dictionary, expected_square_dict)
            self.assertEqual(s2.size, s1.size)
            self.assertEqual(s2.x, s1.x)
            self.assertEqual(s2.id, s1.id)
            self.assertNotEqual(s2, s1)

            """resetting"""
            Base.reset_nb_objects()
