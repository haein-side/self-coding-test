import math
def solution(n, k):
    answer = 0
    jinsu = ''

    while n > 0:
        n, namu = divmod(n, k)
        jinsu += str(namu)

    jinsu = jinsu[::-1]
    num = jinsu.split("0")

    for n in num:
        if n.isdigit():
            n = int(n)
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    break
            else:
                if n != 1:
                    answer += 1

    return answer
