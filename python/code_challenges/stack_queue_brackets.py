from data_structures.queue import Queue


def multi_bracket_validation(string):
    stack = []
    opening = set('([{')
    closing = set(')]}')
    pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in string:
        if char in opening:
            stack.append(char)
        if char in closing:
            if not stack:
                return False
            elif stack.pop() != pair[char]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False
