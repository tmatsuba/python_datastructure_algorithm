# --- coding: utf-8 ---

from  array_sequence.binary_search import binary_search

def uni_char(s):
    u""" 引数で与えられた文字が重複がないかをチェックする関数
    """

    pre = ''
    cur = ''
    lis = sorted(list(s))

    while len(lis) > 0:
        cur = lis.pop(0)

        if pre == cur:
            return False

        pre = cur

    return True
