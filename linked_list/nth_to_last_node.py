# --- coding: utf-8 ---
from linked_list.sinele_linked_list import Node

def nth_to_last_node(head, n):
    u""" 与えられたLinked List のn番目を取得する。
    """
    if n <= 0:
        raise Exception("n must not negative")

    if isinstance(head, Node) == False:
        raise Exception("arg must Node instance")

    cur = head
    cnt = 0

    while n - 1 > 0 and cur is not None:
        cur = cur.nextnode
        n -= 1

    if cur is None:
        raise Exception("index out bounds")

    return cur.value
