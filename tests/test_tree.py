# --- coding: utf-8 ---

from unittest import TestCase
from tree.binary_search_tree import binary_search_tree_check
from tree.binary_search_tree import Tree

class TestBinarySearch(TestCase):

    def test_binary_search_check(self):
        a = Tree(1, 'a')
        b = Tree(2, 'b')
        c = Tree(3, 'c')
        d = Tree(4, 'd')
        e = Tree(5, 'e')
        d.left = b
        b.left = a
        b.right = c
        d.left = e

        self.assertTrue(binary_search_tree_check(a))


        x = Tree(1, 'x')
        y = Tree(2, 'y')
        z = Tree(3, 'z')
        y.left = z
        y.right = x

        self.assertFalse(binary_search_tree_check(y))

        root= Tree(10, "Hello")
        root.left = Tree(5, "Five")
        root.right= Tree(30, "Thirty")
        self.assertTrue(binary_search_tree_check(root))

        root = Tree(10, "Ten")
        root.right = Tree(20, "Twenty")
        root.left = Tree(5, "Five")
        root.left.right = Tree(15, "Fifteen")
        self.assertFalse(binary_search_tree_check(root))
