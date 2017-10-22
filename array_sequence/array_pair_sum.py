# --- coding: utf-8 ---

import math
from  array_sequence.binary_search import binary_search


def pair_sum(lis, sum):
    u""" 引数で与えられたListの中からsumになるペアの数を返す関数
    """

    sorted_list = sorted(lis)
    count = 0
    while len(sorted_list) > 1:
        index = binary_search(sorted_list, sum - sorted_list.pop(0))

        if index >= 0:
            sorted_list.pop(index)
            count += 1

    return count
