#!/usr/bin/python3
"""Unit teting of the Rectnagle Class"""


import unittest
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    def test_valid_attributes(self):
        """Test if the input data is valid
        Only positive integers allowed
        """
        rect = Rectangle(10, 8, 4, 2)
        self.assertIsInstance(rect.width, int)

    def test_valid_height(self):
        rect = Rectangle(10, 8, 4, 2)
        self.assertIsInstance(rect.height, int)

    def test_valid_x(self):
        rect = Rectangle(10, 8, 4, 2)
        self.assertIsInstance(rect.x, int)

    def test_valid_y(self):
        rect = Rectangle(10, 8, 4, 2)
        self.assertIsInstance(rect.y, int)

    def test_width_execption(self):
        with self.assertRaises(TypeError):
            rect = Rectangle('10', 8, 4, 2)

    def test_height_exception(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, '8', 4, 2)

    def test_x_exception(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 8, '4', 2)

    def test_y_exception(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 8, 4, '2')

    def test_width_pos(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 8, 4, 2)

    def test_height_pos(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -8, 4, 2)

    def test_x_pos(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 8, -4, 2)

    def test_y_pos(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 8, 4, -2)

    """Are Test Cases"""
    def test_rect_area(self):
        """
        testing the area of the rectangle
        """
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_area_with_coordinates(self):
        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_rect_with_zero_with(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0,5, 2, 2)

    def test_rect_with_negative_width(self):
        rect = Rectangle(10, 10, 2, 0)
        self.assertEqual(rect.area(), 100)

    """Testing rectangle display"""
    def test_display(self):
        rect = Rectangle(5, 3, 1, 2)
        output = io.StringIO()
        sys.stdout = output
        rect.display()
        display_output = output.getvalue()
        sys.stdout = sys.__stdout__
        expected = "\n\n #####\n #####\n #####\n"
        self.assertEqual(display_output, expected)

    def test_display_with_no_pos(self):
        rect = Rectangle(3, 3, 0, 0)
        output = io.StringIO()
        sys.stdout = output
        rect.display()
        display_output = output.getvalue()
        sys.stdout = sys.__stdout__
        expected = "###\n###\n###\n"
        self.assertEqual(display_output, expected)

    def test_display_with_no_width_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 0, 1, 1)

    def test_display_neg_width_(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-3, -2, 0, 0)

    def test_dsiplay_with_str(self):
        with self.assertRaises(TypeError):
            rect = Rectangle('c', 2, 3, 0)

    def test_display_with_no_y(self):
        rect = Rectangle(5, 2, 2, 0)
        output = io.StringIO()
        sys.stdout = output
        rect.display()
        display_output = output.getvalue()
        sys.stdout = sys.__stdout__
        expected = "  #####\n  #####\n"
        self.assertEqual(display_output, expected)

    """__stt__ Test cases"""

    def test_str_all_positive_input(self):
        rect = Rectangle(10, 2, 3, 5, 10)
        expected = "[Rectangle] (10) 3/5 - 10/2"
        self.assertEqual(str(rect), expected)

    def test_str_with_no_id_param(self):
        rect = Rectangle(5, 3, 1, 2)
        expected = "[Rectangle] (6) 1/2 - 5/3"
        self.assertEqual(str(rect), expected)

    def test_str_all_zero_params(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 0, 0, 0, 2)

    def test_str_no_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 2, 5, 2, 1)
