# --- coding: utf-8 ---

from unittest import TestCase
from  array_sequence.string_compression import string_compression

class TestStringCompression(TestCase):

    def test_string_compression(self):
        self.assertEqual(string_compression(''),'')
        self.assertEqual(string_compression('AABBCC'), 'A2B2C2')
        self.assertEqual(string_compression('AAABCCDDDDD'), 'A3B1C2D5')
