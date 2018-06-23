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

    while cur is not None:
        lis.append(cur)
        cur = cur.nextnode

    if len(lis) < n:
        raise Exception("index out bounds")

    return lis[len(lis) - n]
