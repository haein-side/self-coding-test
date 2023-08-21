import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ground = [[] for _ in range(n)]
high = -1

answer = 1

for i in range(n):
    ground[i] = list(map(int, input().split()))
    if high < max(ground[i]):
        high = max(ground[i])

def bfs(height):
    queue = deque([(0, 0)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    while queue:
        cx, cy = queue.popleft()

        for i in ground[cx][cy]:
            if ground[cx][cy] <= height: # 잠김
                continue
            else: # 안 잠김





for i in range(1, high + 1):
    tmp_result = bfs(i)
    if tmp_result > answer:
        answer = tmp_result

print(answer)