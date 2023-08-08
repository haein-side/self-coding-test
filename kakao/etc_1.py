from collections import defaultdict
def solution(C):
    answer = ''

    dict = defaultdict(list)
    k = -1

    for cmd in C:
        if cmd[0] == "BACK":
            if k - cmd[1] < 0:
                k = 0
            else:
                k -= cmd[1]
        elif cmd[0] == "NEXT":
            if k + cmd[1] > len(dict) - 1:
                k = len(dict) - 1
            else:
                k += cmd[1]
        elif cmd[0] == "PUSH":
            k += 1
            dict[k] = [cmd[1]]
            tmp = len(dict)-1
            if tmp > k:
                for i in range(tmp, k, -1):
                    dict.pop(i)

        # if ind - cmd[1] < 0:
        #     ind = 0
        # elif ind >= len(H):
        #     ind = len(H)-1

        # if i == "BACK":
        #     ind -= 1
        # else:
        #     ind += 1


    answer = dict[k][0]
    return answer

print(solution([["PUSH","www.google.com"],["PUSH","www.yahoo.com"]]))
