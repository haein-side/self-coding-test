import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = []

for i in range(len(arr)):
    if arr[i] - (n - i) >= 0:
        tmp.append(arr[i] - (n-i))
    else:
        tmp.append(0)

print(max(tmp))