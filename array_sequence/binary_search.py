# --- coding: utf-8 ---

import math

def binary_search(lis, val):
    u""" 引数で与えられたListの中から検索valの位置を検索して返す。
    検索値が存在しない場合は-1を返す
    """

    length = len(lis)
    if length == 0:
        return -1

    mid = math.floor(length / 2)

    return _search_array(lis, val, mid, 0, length - 1)

def _search_array(lis, val, mid, src, end):
    if src == end  and lis[mid] != val:
        return -1

    for i in lis:
        if lis[mid] == val:
            return mid

        elif lis[mid] > val:
            return _search_array(lis, val, math.floor((mid - src) / 2) + src, src, mid - 1)

        else:
            return _search_array(lis, val, mid + math.floor((end - mid )  / 2 ) + 1, mid + 1, end)

    return -1
