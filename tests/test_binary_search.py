# --- coding: utf-8 ---

from unittest import TestCase
from  array_sequence.binary_search import binary_search

class TestBinarySearch(TestCase):

    def test_binary_search(self):
        arr = sorted([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1])
        self.assertEqual(binary_search(arr, -1), 0)
        self.assertEqual(binary_search(arr, 1), 1)
        self.assertEqual(binary_search(arr, 2), 2)
        self.assertEqual(binary_search(arr, 3), 3)
        self.assertEqual(binary_search(arr, 4), 4)
        self.assertEqual(binary_search(arr, 5), 5)
        self.assertEqual(binary_search(arr, 6), 7)
        self.assertEqual(binary_search(arr, 7), 8)
        self.assertEqual(binary_search(arr, 8), 9)
        self.assertEqual(binary_search(arr, 9), 10)
        self.assertEqual(binary_search(arr, 11), 11)
        self.assertEqual(binary_search(arr, 13), 13)
        self.assertEqual(binary_search(arr, 14), 14)

        self.assertEqual(binary_search(arr, 10), -1)
        self.assertEqual(binary_search(arr, 15), -1)
        self.assertEqual(binary_search(arr, -2), -1)


        arr = sorted([1,2])
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 2), 1)

        arr = sorted([1])
        self.assertEqual(binary_search(arr, 1), 0)

        arr = sorted([])
        self.assertEqual(binary_search(arr, 1), -1)
