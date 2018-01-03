# --- coding: utf-8 ---

from unittest import TestCase
from linked_list.sinele_linked_list import Node
from linked_list.single_linked_list_cycle_check import cycle_check

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

#Edge case
v = None

class TestAnagram(TestCase):

    def test_anagram(self):
        self.assertTrue(cycle_check(a))
        self.assertFalse(cycle_check(x))
        self.assertFalse(cycle_check(v))
