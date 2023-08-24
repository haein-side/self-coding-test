import sys
input = sys.stdin.readline

def match(name1, name2):
    n1 = len(name1)
    n2 = len(name2)
    for k in range(1, min(n1,n2) + 1):
        if name1[:k] == name2[n2-k:]:
            return 1
        if name2[:k] == name1[n1-k:]:
            return 1
    return 0

n = int(input())
names = []
ans = 0
for i in range(n):
    name1 = input().rstrip()
    for name2 in names:
        ans += match(name1, name2)
    names.append(name1)

print(ans)
