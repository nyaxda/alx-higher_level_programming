#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
import json


class TestRectangle(unittest.TestCase):
    """test for rectangle class"""
    def test_normal_cases(self):
        """normal test cases"""
        r1 = Rectangle(6, 10)
        r2 = Rectangle(5, 10, 3)
        r3 = Rectangle(5, 10, 3, 4)

        self.assertEqual(r1.area(), 60)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

        """resetting"""
        Base.reset_nb_objects()

    def test_exceptions(self):
        """testing for exceptions"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 10)
        with self.assertRaises(TypeError):
            r2 = Rectangle("5", 10)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, -10)
        with self.assertRaises(TypeError):
            r4 = Rectangle(5, "10")
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, 10, -1)
        with self.assertRaises(TypeError):
            r6 = Rectangle(5, 10, "1")
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, 10, 1, -1)
        with self.assertRaises(TypeError):
            r6 = Rectangle(5, 10, 1, "1")
        with self.assertRaises(TypeError):
            r7 = Rectangle()
        with self.assertRaises(TypeError):
            r8 = Rectangle(20)
        with self.assertRaises(TypeError):
            r8 = Rectangle(20, 10, 5, 2, 3, 7)

        """resetting"""
        Base.reset_nb_objects()

    def test_display(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)
        r3 = Rectangle(2, 2, 1)
        r4 = Rectangle(3, 3, 1, 5)

        original_output = sys.stdout

        try:
            # stdout to StringIO object
            sys.stdout = StringIO()
            r1.display()
            output = sys.stdout.getvalue()
            # testing output
            self.assertEqual(output, '####\n' * 6)
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

            r2.display()
            output = sys.stdout.getvalue()
            self.assertEqual(output, '##\n' * 2)
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

            r3.display()
            output = sys.stdout.getvalue()
            # testing output
            self.assertEqual(output, ' ##\n' * 2)

            sys.stdout.seek(0)
            sys.stdout.truncate(0)
            r4.display()
            output = sys.stdout.getvalue()
            # testing output
            self.assertEqual(output, '\n' * 5 + ' ###\n' * 3)

        finally:
            # restoring stdout to original value
            sys.stdout = original_output

        """resetting"""
        Base.reset_nb_objects()

        def test_str(self):
            r1 = Rectangle(4, 6)
            r2 = Rectangle(2, 2)
            r3 = Rectangle(2, 2, 1)
            r4 = Rectangle(3, 3, 1, 5)

            self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 4/6")
            self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 2/2")
            self.assertEqual(str(r3), "[Rectangle] (3) 1/0 - 2/2")
            self.assertEqual(str(r4), "[Rectangle] (4) 1/5 - 3/3")

            """resetting"""
            Base.reset_nb_objects()

        def test_update(self):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89)
            self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
            r1.update(89, 2)
            self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
            r1.update(89, 2, 3)
            self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
            r1.update(89, 2, 3, 4)
            self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
            r1.update(89, 2, 3, 4, 5)
            self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

            """resetting"""
            Base.reset_nb_objects()

        def test_kwarg_updates(self):
            r1 = Rectangle(10, 10, 10, 10)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
            r1.update(height=1)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
            r1.update(width=1, x=2)
            self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
            r1.update(y=1, width=2, x=3, id=89)
            self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
            r1.update(x=1, height=2, y=3, width=4)
            self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

            """resetting"""
            Base.reset_nb_objects()

    def test_dictionary_representation(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}

        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(r2.width, r1.width)
        self.assertEqual(r2.height, r1.height)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.id, r1.id)
        self.assertNotEqual(r2, r1)

        """resetting"""
        Base.reset_nb_objects()

    def test_dict_to_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        expected_rect_dictionary = {
            'x': 2, 'width': 10,
            'id': 1, 'height': 7, 'y': 8
            }

        expected_dict = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(dictionary, expected_rect_dictionary)
        self.assertEqual(json.loads(json_dictionary), expected_dict)

        """resetting"""
        Base.reset_nb_objects()

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        expected_output = [{
            "y": 8,
            "x": 2,
            "id": 1,
            "width": 10,
            "height": 7},
            {"y": 0,
             "x": 0,
             "id": 2,
             "width": 2,
             "height": 4
             }]
        with open("Rectangle.json", "r") as file:
            content = json.load(file)
            self.assertEqual(content, expected_output)

        """resetting"""
        Base.reset_nb_objects()

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertIsInstance(json_list_input, str)
        self.assertEqual(json.loads(json_list_input), list_input)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)

    def test_dictionary_to_instance(self):
        r1 = Rectangle(3, 5, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r1_dictionary, dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1_dictionary, r2.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1_dictionary, r2)

        """resetting"""
        Base.reset_nb_objects()

    def test_file_to_instances(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()

        self.assertIsInstance(list_input, list)
        self.assertIsInstance(list_output, list)
        self.assertNotEqual(list_input, list_output)
        self.assertNotEqual(list_input[0], list_output[0])
        self.assertNotEqual(list_input[1], list_output[1])

        """resetting"""
        Base.reset_nb_objects()
