def solution(S):
    answer = ''
    pair = {')' : '(', ']' : '[', '}': '{'}

    stack = []

    for char in S:
        if char in '({[':
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if (pair[char] != top):
                    return "FALSE"
            else:
                return "FALSE"

    return "TRUE"


print(solution("(){}]"))
