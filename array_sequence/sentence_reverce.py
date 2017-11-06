# --- coding: utf-8 ---

def sentence_reverce(str):
    u"""センテンスを逆順に並べ換えた文字列を返す
    """
    if len(str.strip()) == 0:
        return

    arr = str.split()
    rev_arr = []
    rev = ''

    for word in arr:
        rev_arr.append(word)

    return ' '.join(reversed(rev_arr))
