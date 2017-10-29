from unittest import TestCase
from  array_sequence.anagram import anagram

class TestAnagram(TestCase):

    def test_anagram(self):
        self.assertTrue(anagram('dog', 'god'))
        self.assertTrue(anagram('clint eastwood','old west action'))
        self.assertFalse(anagram('aa','bb'))
        self.assertTrue(anagram('go go go','gggooo'))
        self.assertTrue(anagram('abc','cba'))
        self.assertTrue(anagram('hi man','hi     man'))
        self.assertFalse(anagram('aabbcc','aabbc'))
        self.assertFalse(anagram('123','1 2'))
        self.assertTrue(anagram('Aabbcc','aaBbcc'))
        self.assertFalse(anagram('123','1234'))
