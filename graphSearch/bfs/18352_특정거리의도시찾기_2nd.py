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

'''
visited 따져야 하는 이유 좀 했갈렸음
단방향이긴 하지만 최단 거리를 구하므로..
다시 왕복해서 돌아올 수도 있음. 그때 못 오게 하려면 visited 필요
'''
