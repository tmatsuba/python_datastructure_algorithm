# --- coding: utf-8 ---

from unittest import TestCase
from  array_sequence.finder import finder, finder2

class TestAnagram(TestCase):

    def test_finder(self):
        self.assertEqual(finder([5,5,7,7],[5,7,7]),5)
        self.assertEqual(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        self.assertEqual(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)

        self.assertEqual(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6, 1]), None)

    def test_finder2(self):
        self.assertEqual(finder2([5,5,7,7],[5,7,7]),5)
        self.assertEqual(finder2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        self.assertEqual(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)

        self.assertEqual(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6, 1]), None)
