from unittest import TestCase
from  array_sequence.uni_char import uni_char

class TestUniChar(TestCase):

    def test_uni_char(self):
        self.assertTrue(uni_char(''))
        self.assertFalse(uni_char('goo'))
        self.assertTrue(uni_char('abcdefg'))

