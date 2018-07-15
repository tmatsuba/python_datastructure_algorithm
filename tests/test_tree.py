# --- coding: utf-8 ---

from unittest import TestCase
from tree.binary_search_tree import binary_search_tree_check, levelOrderPrint, levelOrderPrint2, trimBST
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
        self.assertEqual(levelOrderPrint2(d), assert_str)

    def test_trimBST(self):
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

        g = trimBST(d, 2, 5)
        self.assertEqual(g.val, 4)
        self.assertEqual(g.left.val, 2)
        self.assertEqual(g.left.right.val, 3)
        self.assertEqual(g.left.left, None)
        self.assertEqual(g.right.val, 5)
        self.assertEqual(g.right.right, None)

        a = Node(8)
        b = Node(3)
        c = Node(1)
        d = Node(6)
        e = Node(4)
        f = Node(7)
        g = Node(10)
        h = Node(14)
        i = Node(13)

        a.left = b
        a.right = g
        b.left = c
        b.right = d
        d.left = e
        d.right = f
        g.right = h
        h.left = i

        j = trimBST(a, 5, 13)
        self.assertEqual(j.val, 8)
        self.assertEqual(j.left.val, 6)
        self.assertEqual(j.left.right.val, 7)
        self.assertEqual(j.left.left, None)
        self.assertEqual(j.right.val, 10)
        self.assertEqual(j.right.right.val, 13)
        self.assertEqual(j.right.right.left, None)
