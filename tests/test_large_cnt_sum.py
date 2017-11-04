# --- coding: utf-8 ---

from unittest import TestCase
from  array_sequence.large_cnt_sum import large_cnt_sum

class TestLargeCntSum(TestCase):

    def test_large_cnt_sum(self):
        self.assertEqual(large_cnt_sum([1,2,-1,3,4,10,10,-10,-1]), 29)
        self.assertEqual(large_cnt_sum([]), None)
        self.assertEqual(large_cnt_sum([1,2,-1,3,4,-1]),9)
        self.assertEqual(large_cnt_sum([1,2,-1,3,4,10,10,-10,-1]),29)
        self.assertEqual(large_cnt_sum([-1,1]),1)
