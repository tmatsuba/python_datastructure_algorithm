# --- coding: utf-8 ---

from unittest import TestCase
from linked_list.sinele_linked_list import Node
from linked_list.nth_to_last_node import nth_to_last_node

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

class TestNthToLastNode(TestCase):

    def test_nth_to_last_node(self):

        self.assertEqual(a.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 4)

        self.assertEqual(nth_to_last_node(a, 1), 1)
        self.assertEqual(nth_to_last_node(a, 2), 2)
        self.assertEqual(nth_to_last_node(a, 3), 3)
        self.assertEqual(nth_to_last_node(a, 4), 4)

        with self.assertRaises(Exception):
            nth_to_last_node(a, -1)
            nth_to_last_node(None, 1)
            nth_to_last_node(a, 100)
