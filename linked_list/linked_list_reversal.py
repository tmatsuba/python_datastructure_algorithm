# --- coding: utf-8 ---
from linked_list.sinele_linked_list import Node

def reverse(head):
    u""" 与えられたLinked List を逆順にLinkさせる
    """
    if isinstance(head, Node) == False:
        raise Exception("arg must Node instance")

    cur = head
    next = None
    prev = None

    while cur != None:
        next = cur.nextnode
        cur.nextnode = prev

        prev = cur
        cur = next
