import unittest

from Lesson_8 import adder

class MyTest(unittest.TestCase):

    def test_args(self):
        self.assertEqual(adder(2,2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)

    def test_mixed(self):
        self.assertEqual(
            adder(1, 2, a=10, b=11), 24
        )

    def test_diff_numbers(self):
        x = 10
        y = 0
        self.assertEqual(
            adder(0, -5, y, i=x), 5
        )

    def test_wrong_data(self):
        self.assertEqual(
            adder('5', 'abc', 10), 15
        )