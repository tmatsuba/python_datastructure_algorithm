# --- coding: utf-8 ---

from  array_sequence.binary_search import binary_search


def pair_sum(lis, sum):
    u""" 引数で与えられたlisの中からsumになるペアの数を返す関数
    """
    if len(lis) < 2:
        return

    sorted_list = sorted(lis)
    count = 0
    while len(sorted_list) > 1:
        index = binary_search(sorted_list, sum - sorted_list.pop(0))

        if index >= 0:
            sorted_list.pop(index)
            count += 1

    return count

def pair_sum2(arr, k):
    u""" 引数で与えられたarrの中からkになるペアの数を返す関数
    """

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)

        else:
            output.add( (min(num, target), max(num, target)) )
    return len(output)
