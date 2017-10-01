from unittest import TestCase
from dynamic_array.dynamic_array import DynamicArray

class TestDynamicArray(TestCase):

    def test_zero(self):
        c = DynamicArray()
        self.assertEqual(len(c), 0)

    def test_arrays(self):
        c = DynamicArray()

        for i in range(100):
            c.append(i)
            self.assertEqual(len(c), i + 1)            
