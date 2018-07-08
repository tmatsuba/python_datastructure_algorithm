# --- coding: utf-8 ---

class Tree:
    def __init__(self, key, value):
         self.key = key
         self.right = None
         self.left = None

    def setRight(self, tree):
        self.right = tree
    def setLeft(self, tree):
        self.left = left


def binary_search_tree_check(tree):
    u""" Binary Search Treeとして正しいかを検証する関数
    """

    if tree.left:
        if tree.key < tree_max(tree.left):
            return False
        if not binary_search_tree_check(tree.left):
            return False

    if tree.right:
        if tree.key > tree_min(tree.right):
            return False

        if not binary_search_tree_check(tree.right):
            return False

    return True

def tree_max(tree):
    if not tree:
        return float('-inf')

    max_left = tree_max(tree.left)
    max_right = tree_max(tree.right)
    return max(max_left, max_right, tree.key)


def tree_min(tree):
    if not tree:
        return float('inf')

    min_left = tree_min(tree.left)
    min_right = tree_min(tree.right)
    return min(min_left, min_right, tree.key)
