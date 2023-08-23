'''
벽을 세 개 세우기
벽이 세 개이면 dfs를 돌리기
dfs에서 돌아다녀야 하는 원소는 바이러스인 것
상하좌우로 돌아다니면서 해당 원소가 0이면 2로 만들기
그렇게 그래프를 생성하고 (바이러스가 퍼진 것)
전체 for문을 돌면서 0인 것의 개수 세고 dfs 함수 리턴할 것
'''
import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []

mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
    tmp_graph = copy.deepcopy(graph)
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        cx, cy = queue.popleft()
        for a, b in mov:
            mx, my = cx + a, cy + b
            if 0 <= mx < n and 0 <= my < m:
                if tmp_graph[mx][my] == 0:
                    tmp_graph[mx][my] = 2
                    queue.append((mx, my))

    tmp_answer = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                tmp_answer += 1

    return tmp_answer



def make_wall(cnt):
    if cnt == 3:
        answer.append(bfs())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

make_wall(0)

print(max(answer))