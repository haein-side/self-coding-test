def solution(S):
    pair = {"}": "{", ")": "(", "]": "["}

    stack = []
    arr = []
    is_comment = False
    for i in range(len(S)):
        if S[i:i+2] == "/*":
            is_comment = True
            continue
        if S[i:i+2] == "*/":
            is_comment = False
            continue
        if is_comment:
            continue
        arr.append(S[i])

    if len(arr) == 0:
        return False

    for char in arr:
        # 문자가 여는 괄호라면
        if char in pair.values():
            # 스택에 삽입
            stack.append(char)
        # 문자가 닫는 괄호라면
        else:
            # 스택에 열린 괄호가 남아있다면
            if stack:
                # 스택 top의 열린 괄호
                top = stack.pop()
                # 닫힌 괄호와 스택 top의 열린 괄호가 짝이 안 맞는다면
                if pair[char] != top:
                    return False
            # 스택이 비어 있다면
            else:
                return False

    if stack:
        return False
    else:
        return True

print(solution(['(/*(){})[*/]']))
print(solution(['(/*()}*/[{}])']))
print(solution(['(){/**/}[[()]]']))
print(solution(['{}[]']))
