#You may use import as below.
# import math

def solution(num):
    # Write code here.
    # num + 1 한 것에서 0은 1로 바꾼 것 return
    num += 1
    answer = list(str(num))
    for idx, n in enumerate(answer):
        if n == '0':
            answer[idx] = '1'
    result = int(''.join(answer))
    return result

#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")