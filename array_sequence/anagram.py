
def anagram(s1,s2):
    sorted_s1 = sorted(s1.replace(" ", ""))
    sorted_s2 = sorted(s2.replace(" ", ""))

    return sorted_s1 == sorted_s2

