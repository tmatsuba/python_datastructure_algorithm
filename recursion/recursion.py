# --- coding: utf-8 ---

def reverse(value, ret = ''):
    u""" 与えられた文字列を逆順にする
    """
    if value == '':
        return ret

    return reverse(value[:len(value) - 1], ret + value[-1])

