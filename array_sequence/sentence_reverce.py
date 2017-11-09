# --- coding: utf-8 ---

def sentence_reverce(str):
    u"""センテンスを逆順に並べ換えた文字列を返す
    """
    if len(str.strip()) == 0:
        return

    return ' '.join(reversed(str.split()))
