# --- coding: utf-8 ---

from unittest import TestCase
from tree.binary_search_tree import binary_search_tree_check, levelOrderPrint, levelOrderPrint2
from tree.binary_search_tree import Tree, Node

class TestTree(TestCase):

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

    def test_level_order_print(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        f = Node(6)
        d.left = b
        b.left = a
        b.right = c
        d.right = e
        e.right = f

        assert_str = '4 \n' + '2 5 \n' + '1 3 6 \n'

        self.assertEqual(levelOrderPrint(d), assert_str)
        self.assertEqual(levelOrderPrint2(d), assert_str)ma
