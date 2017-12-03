# --- coding: utf-8 ---


def string_compression(s):
    u"""与えられた文字の出現回数を返す"""

    if len(s) == 0:
        return ''

    sorted_str = sorted(s)
    i = 1
    cnt = 0
    c = sorted_str[0]
    ret = ''

    while i < len(sorted_str):
        cnt += 1
        if c != sorted_str[i]:
            ret = ret + c + str(cnt)
            c = sorted_str[i]
            cnt = 0

        i += 1


    return ret + c + str(cnt + 1)
