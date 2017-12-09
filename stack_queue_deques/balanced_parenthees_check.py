# --- coding: utf-8 ---

def balanced_parenthees_check(val):
    u"""かっこのバランスをチェックする関数
    かっこ以外の文字は許容しない。
    """

    if len(val) % 2 != 0:
        return False

    check_list = list(val)

    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']

    stack_list = []

    while check_list != []:
        c = check_list.pop(0)

        if c in open_list:
            stack_list.append(c)
        elif c in close_list:
            index = close_list.index(c)

            if len(stack_list) == 0:
                return False

            if stack_list.pop() != open_list[index]:
                return False

        else:
            return False

    return len(stack_list) == 0
