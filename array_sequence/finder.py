# --- coding: utf-8 ---
from array_sequence.binary_search import binary_search

def finder(arr1, arr2):
    u"""arr1のうち、arr2に存在しない値を1つ表示する
    """

    if (len(arr1) - len(arr2)) != 1:
        return

    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    for src in sorted_arr1:
        index = binary_search(sorted_arr2, src)
        if index < 0:
            return src
        else:
            sorted_arr2.pop(index)

def finder2(arr1, arr2):
    u"""arr1のうち、arr2に存在しない値を1つ表示する
    """

    if (len(arr1) - len(arr2)) != 1:
        return

    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    for num1, num2 in zip(sorted_arr1, sorted_arr2):
        if num1 != num2:
            return num1

    return sorted_arr1[-1]
