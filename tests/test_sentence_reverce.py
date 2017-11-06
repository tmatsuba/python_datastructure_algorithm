# --- coding: utf-8 ---

from unittest import TestCase
from  array_sequence.sentence_reverce import sentence_reverce

class TestSentenceReverce(TestCase):

    def test_sentence_reverce(self):
        self.assertEqual(sentence_reverce('    space before'),'before space')
        self.assertEqual(sentence_reverce('space after     '),'after space')
        self.assertEqual(sentence_reverce('   Hello John    how are you   '),'you are how John Hello')
        self.assertEqual(sentence_reverce('1'),'1')
        self.assertEqual(sentence_reverce(''),None)
        self.assertEqual(sentence_reverce('    '),None)
