
def solution(num):
    origin_number = []
    for i in range(len(num)):
        origin_number.append(int(num[i]))

    before = -1
    cnt = 0
    # for i in origin_number:
    #     if before == -1:
    #         before = i
    #         cnt += 1
    #         print(i, '위', cnt)
    #     else:
    #         if before + 1 == i and before != 0:
    #             print(i, '아래1', cnt)
    #             before = -1
    #             continue
    #         else:
    #             before = i
    #             cnt += 2
    #             print(i, '아래2', cnt)
    #
    # return cnt




print(solution("12156"))
print(solution("321"))
