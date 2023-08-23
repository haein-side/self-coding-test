import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0
odd = []

for i in arr:
    if i % 2 == 0:
        answer += i
    else:
        odd.append(i)

if len(odd) % 2 == 0:
    answer += sum(odd)
else:
    answer += sum(odd) - odd[0]

print(answer)