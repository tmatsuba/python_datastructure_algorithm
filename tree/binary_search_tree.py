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

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val

def levelOrderPrint(tree):
    u""" 同じ高さ毎に値を出力する関数
    """

    lis = []
    lis.append(tree)
    return getLevelList(lis, str(tree.val))

def getLevelList(lis, str_ret):
    if not lis:
        return str_ret

    next_list = []
    str_list = []
    for i in lis:
        if i.left:
            str_list.append(str(i.left.val))
            next_list.append(i.left)

        if i.right:
            str_list.append(str(i.right.val))
            next_list.append(i.right)
    return getLevelList(next_list, str_ret +' \n'  + ' '.join(str_list))

import collections

def levelOrderPrint2(tree):
    u""" 同じ高さ毎に値を出力する関数(解答編より)
    """

    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    ret = ''
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        #print(currentNode.val, end = ' ')
        ret = ret + str(currentNode.val) + ' '
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            ret +=  '\n'
            currentCount, nextCount = nextCount, currentCount
    return ret
