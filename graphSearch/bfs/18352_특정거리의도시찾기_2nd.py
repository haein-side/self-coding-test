import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)


def bfs(start_v):
    queue = deque([start_v])
    visited = [-1 for _ in range(n)]
    visited[start_v] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == -1 or v == start_v:
                visited[i] = visited[v] + 1
                queue.append(i)

    return visited


distance = bfs(x - 1)
flag = False
for i in range(len(distance)):
    if distance[i] == k:
        flag = True
        print(i+1)

if not flag:
    print(-1)
