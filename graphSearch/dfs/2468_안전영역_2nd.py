import sys

input = sys.stdin.readline

n = int(input())
ground = [[] for _ in range(n)]
high = -1

answer = 1

for i in range(n):
    ground[i] = list(map(int, input().split()))
    if high < max(ground[i]):
        high = max(ground[i])


def dfs(x, y, tmp_visited, rain):
    stack = [(x, y)]
    tmp_visited[x][y] = 1
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while stack:
        cx, cy = stack.pop()
        for mx, my in move:
            nx, ny = cx + mx, cy + my
            if 0 <= nx < n and 0 <= ny < n:
                if ground[nx][ny] > rain and tmp_visited[nx][ny] == -1:
                    tmp_visited[nx][ny] = 1
                    stack.append((nx, ny))

tmp_answer = []

for i in range(0, high + 1):
    cnt = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if ground[j][k] > i and visited[j][k] == -1:
                cnt += 1
                dfs(j, k, visited, i)
    tmp_answer.append(cnt)

print(max(tmp_answer))