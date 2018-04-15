# --- coding: utf-8 ---

from unittest import TestCase
from linked_list.sinele_linked_list import Node
from linked_list.linked_list_reversal import reverse

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

#Edge case
v = None

class TestLinkedListReversal(TestCase):

    def test_reverse(self):

        self.assertEqual(a.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 4)

        reverse(a)

        self.assertEqual(b.nextnode.value, 1)
        self.assertEqual(c.nextnode.value, 2)
        self.assertEqual(d.nextnode.value, 3)

        with self.assertRaises(Exception):
            reverse('hoge')
