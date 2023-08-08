import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b-1].append(a-1)


def dfs(start_v):
    visited = [0 for _ in range(n)]
    stack = [start_v]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for k in graph[v]:
                stack.append(k)

    return visited.count(1) - 1


result = [0 for _ in range(n)]
for i in range(n):
    result[i] = dfs(i)

answer = []
a = max(result)
for i in range(n):
    if result[i] == a:
        answer.append(i+1)

print(' '.join(map(str, answer)))

'''
pypy로 돌리니까 시간초과 안 나긴 했음
그러나 bfs 코드와 비교 했을 때 11424ms -> 15124ms가 걸림
'''
