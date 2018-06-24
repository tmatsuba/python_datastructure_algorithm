# --- coding: utf-8 ---

from unittest import TestCase
from linked_list.sinele_linked_list import Node
from linked_list.nth_to_last_node import nth_to_last_node, nth_to_last_node2

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

#Edge case
v = None

class TestNthToLastNode(TestCase):

    def test_nth_to_last_node(self):

        self.assertEqual(a.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 4)

        self.assertEqual(nth_to_last_node(1, a), e)
        self.assertEqual(nth_to_last_node(2, a), d)
        self.assertEqual(nth_to_last_node(3, a), c)
        self.assertEqual(nth_to_last_node(4, a), b)

        with self.assertRaises(Exception):
            nth_to_last_node(-1, a)
            nth_to_last_node(1, None)
            nth_to_last_node(100, a)

    def test_nth_to_last_node2(self):

        self.assertEqual(a.nextnode.value, 2)
        self.assertEqual(b.nextnode.value, 3)
        self.assertEqual(c.nextnode.value, 4)

        self.assertEqual(nth_to_last_node2(1, a), e)
        self.assertEqual(nth_to_last_node2(2, a), d)
        self.assertEqual(nth_to_last_node2(3, a), c)
        self.assertEqual(nth_to_last_node2(4, a), b)

        with self.assertRaises(Exception):
            nth_to_last_node2(-1, a)
            nth_to_last_node2(1, None)
            nth_to_last_node2(100, a)
