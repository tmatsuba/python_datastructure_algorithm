# --- coding: utf-8 ---

from unittest import TestCase
from  stack_queue_deques.balanced_parenthees_check import balanced_parenthees_check

class TestBalancedQueueDeque(TestCase):

    def test_balanced_parenthees_check(self):
        self.assertFalse(balanced_parenthees_check('[](){([[[]]])}('))
        self.assertTrue(balanced_parenthees_check('[{{{(())}}}]((()))'))
        self.assertFalse(balanced_parenthees_check('[[[]])]'))
        self.assertTrue(balanced_parenthees_check(''))
        self.assertFalse(balanced_parenthees_check('[]{'))

