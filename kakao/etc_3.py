def solution(S):
    pair = {"}":"{", ")":"(", "]":"["}

    S = "".join(S)
    stack = []
    arr = []
    check = False

    for i in range(len(S)):
        if S[i:i+2] == "/*":
            check = True
        if S[i:i+2] == "*/":
            check = False
        # print(i, S[i:i+2], check)
        if check:
            continue
        else:
            if S[i:i+2] != "*/" and S[i] != "/":
                arr.append(S[i])

    print(arr)

    if len(arr) == 0:
        return "FALSE"

    for char in arr:
        if char not in pair.keys() and char not in pair.values():
            continue
        # 문자가 여는 괄호라면
        if char in pair.values():
            # 스택에 삽입
            stack.append(char)
        # 문자가 닫는 괄호라면
        else:
            # 스택에 열린 괄호가 남아있다면
            if (stack):
                # 스택 top의 열린 괄호
                top = stack.pop()
                # 닫힌 괄호와 스택 top의 열린 괄호가 짝이 안 맞는다면
                if (pair[char] != top):
                    return "FALSE"
            # 스택이 비어 있다면
            else:
                return "FALSE"

    print(stack)

    return "TRUE"

print(solution(['(/*(){})[*/]'])) # F
print(solution(['(/*()}*/[{}])'])) # T
print(solution(['(){/**/}[[()]]'])) # T
print(solution(['{}[]'])) # T
print(solution(["/*((())*/ {}{} /*((*/))"])) # F
print(solution(["/*((())*/ {}{} /*((*/"])) # T
print(solution(["(/*))*/{{/**/()"]))
