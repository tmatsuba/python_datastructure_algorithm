# --- coding: utf-8 ---

def sentence_reverce(str):
    u"""センテンスを逆順に並べ換えた文字列を返す
    """
    if len(str.strip()) == 0:
        return

    return ' '.join(reversed(str.split()))

def sentence_reverce2(str):
    u"""センテンスを逆順に並べ換えた文字列を返す(split, reversedを使わない)
    """
    if len(str.strip()) == 0:
        return

    length = len(str)
    spaces = [' ', '	']
    words = []
    i = 0

    while i < length:
        if str[i] not in spaces:
            word_start = i

            while i < length and str[i] not in spaces:
                i +=  1
            words.append(str[word_start:i])
        i += 1

    rev_words = []
    i = len(words)

    while i > 0:
        rev_words.append(words[i - 1])
        i -= 1

    return ' '.join(rev_words)
