# --- coding: utf-8 ---

def large_cnt_sum(arr):
    u"""arrを足していき、最大の値を返す。
    足している数より要素の値が大きかったらその値を返す"""
    if len(arr) == 0:
        return

    lis = []
    sum = 0
    for num in arr:
        sum = sum + num

        if sum > num:
             lis.append(sum)
        else:
             lis.append(num)

    return sorted(lis).pop()
