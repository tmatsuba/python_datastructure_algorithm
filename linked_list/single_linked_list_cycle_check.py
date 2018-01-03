from linked_list.sinele_linked_list import Node

def cycle_check(node):
    u""" single linked listが循環しているかをチェックする関数
    """

    first = node
    start = node

    while  start.nextnode is not None:
        if first == start.nextnode:
            return True
        start = start.nextnode

    return False
