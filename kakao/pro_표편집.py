from copy import deepcopy
def solution(n, k, cmd):
    answer = ["X" for _ in range(n)]

    num = [i for i in range(n)] # 현재 리스트 안에 있는 숫자들
    cur = k # 현재 위치
    cleared_num = [] # 삭제된 숫자들

    for order in cmd:
        if "D" in order:
            a, b = order.split()
            cur += int(b)
        if "U" in order:
            a, b = order.split()
            cur -= int(b)
        if "C" in order:
            cleared_num.append((cur, num[cur]))
            if cur == len(num) - 1:
                cur -= 1
                del num[cur+1]
            else:
                del num[cur]
        if "Z" in order:
            ind, cleared = cleared_num.pop()
            if ind < cur:
                cur += 1
            if ind == len(num):
                num.append(cleared)
            else:
                a, b = num[:ind], num[ind:]
                a.append(cleared)
                a += b
                num = a

    for i in num:
        answer[i] = "O"

    return "".join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
