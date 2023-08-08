import sys
import math
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
spot = [[] for _ in range(n + 1)] # n번째 점의 좌표 [x, y]
edges = [[] for _ in range(n + 1)] # n번째 점에서 갈 수 있는 곳(cost, x, y)
edges[0] = [0, 0, 0, 0]
parent = [i for i in range(n + 1)] # 1 ~ n번 점까지

for i in range(n):
    x, y = map(int, input().split())
    spot[i+1] = [x, y]

for i in range(n-1): # 0 ~ n
    for j in range(i+1, n):
        cost = math.sqrt((spot[i+1][0] - spot[j+1][0]) ** 2 + (spot[i+1][1] - spot[j+1][1]) ** 2)
        edges[i+1].append([cost, i+1, j+1, 0])

for i in range(m):
    a, b = map(int, input().split())
    x1, x2, y1, y2 = spot[a][0], spot[b][0], spot[a][1], spot[b][1]
    cost = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    edges.append([cost, a, b, 1])

# print(edges)
# edges.sort(key = lambda x : x[0])

result = 0

for i in range(1, len(edges) + 1):
    cost, x, y, b = edges[i]
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        if b == 0:
            result += cost
            edges[i] = [cost, x, y, 1]

print(result)
