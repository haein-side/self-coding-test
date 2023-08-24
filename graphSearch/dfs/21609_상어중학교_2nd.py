'''
1. 크기가 가장 큰 블록 그룹을 찾아야
- 무지개 블록의 수가 가장 많은 블록 그룹
- 기준 블록의 행이 가장 큰 것
- 열이 가장 큰 것을 찾아야

2. 블록그룹의 모든 불록 제거
- B의 제곱 점 획득

3. 격자에 중력 작용

3. 격자가 90도 반시계 방햐으로 회전

4. 격자에 중력 작용
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, total):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    stack = [(x, y)]
    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    color = graph[x][y] # 일반 블록의 색깔

    while stack:
        cx, cy = stack.pop()

        for i in mv:
            mx, my = cx + i[0], cy + i[1]
            if 0 <= mx < n and 0 <= my < n:
                if graph[mx][my] != -1 and not visited[mx][my]: # 검은색 블록이 아닐 때
                    if graph[mx][my] == 0:  # 일반 블록일 경우 색깔 동일할 때
                        visited[mx][my] = 1
                        stack.append((mx, my))
                    elif graph[mx][my] == color:
                        # total[mx][my] = True
                        visited[mx][my] = 1
                        stack.append((mx, my))

    print(visited)

    return visited


total_visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if 1 <= graph[i][j] <= m and not total_visited[i][j]:
            total_visited = 1
            dfs(i, j, total_visited)