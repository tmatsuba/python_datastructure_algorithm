# --- coding: utf-8 ---
from linked_list.sinele_linked_list import Node

def nth_to_last_node(n , head):
    u""" 与えられたLinked List の後ろからn番目を取得する。
    """
    if n <= 0:
        raise Exception("n must not negative")

    if isinstance(head, Node) == False:
        raise Exception("arg must Node instance")

    cur = head
    cnt = 0
    lis = []

    while cur:
        lis.append(cur)
        cur = cur.nextnode

    if len(lis) < n:
        raise Exception("index out bounds")

    return lis[len(lis) - n]

def nth_to_last_node2(n , head):
    u""" 与えられたLinked List の後ろからn番目を取得する。
    """
    if n <= 0:
        raise Exception("n must not negative")

    if isinstance(head, Node) == False:
        raise Exception("arg must Node instance")

    right_pointer = head
    left_pointer = head

    for i in range(n):
        if not right_pointer.nextnode:
            LookupError("index out bounds")

        right_pointer = right_pointer.nextnode

    while right_pointer:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    return left_pointer
