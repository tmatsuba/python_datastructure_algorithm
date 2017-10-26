# --- coding: utf-8 ---

from  array_sequence.binary_search import binary_search

def anagram(s1,s2):
    sorted_s1 = sorted(s1.replace(" ", ""))
    sorted_s2 = sorted(s2.replace(" ", ""))

    for src in sorted_s1:
        index = binary_search(sorted_s2, src)
        if index >= 0:
            sorted_s2.pop(index)
        else:
            return False

    return len(sorted_s2) == 0

