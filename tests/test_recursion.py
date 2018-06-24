from unittest import TestCase
from recursion.recursion import reverse

class TestRecursion(TestCase):

    def test_reverse(self):
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('hoge'), 'egoh')
        self.assertEqual(reverse('hello'),'olleh')
        self.assertEqual(reverse('hello world'),'dlrow olleh')
        self.assertEqual(reverse('123456789'),'987654321')
