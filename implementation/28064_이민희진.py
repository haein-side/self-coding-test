import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(i+1, n):
        if len(arr[i]) <= len(arr[j]):
            repeat = len(arr[i])
        else:
            repeat = len(arr[j])
        for k in range(repeat):
            if arr[i][:k+1] == arr[j][-k-1:]:
                answer += 1
                break
        else:
            for q in range(repeat):
                if arr[i][-q-1:] == arr[j][:q+1]:
                    answer += 1
                    break


print(answer)

