from collections import deque
def solution(num):
    origin_number = deque([])
    for i in range(len(num)):
        origin_number.append(int(num[i]))

    cnt = 0
    while len(origin_number) >= 1:
        # print(cnt, origin_number)

        now = origin_number.popleft()
        if len(origin_number) == 0 and now != 0:
            cnt += 2
            break
        else:
            if now == 0:
                cnt += 1
            else:
                next = origin_number.popleft()
                if now + 1 ==  next:
                    cnt += 1
                else:
                    origin_number.appendleft(next)
                    cnt += 2

    return cnt



print(solution("12156"))
print(solution("321"))
print(solution("1234567"))
print(solution("100"))
