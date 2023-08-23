import sys
input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(len(arr[i])): # yunny의 철자 수만큼 반복
        for k in range(n):
            print(arr[i][:j], arr[k][-j-1:], i, k)
            if i != k and arr[i][:j] == arr[k][-j-1:]:
                answer += 1

print(answer)
