import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    color = graph[x][y]
    cnt = 1
    blocks = [(x, y)]
    musigae = 0

    while queue:
        cx, cy = queue.popleft()

        for a, b in mv:
            nx, ny = cx + a, cy + b
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != -1 and graph[nx][ny] != -2:
                if graph[nx][ny] == 0: # 무지개 블록
                    cnt += 1
                    blocks.append((nx, ny))
                    visited[nx][ny] = 1
                    musigae += 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == color: # 일반 블록
                    cnt += 1
                    blocks.append((nx, ny))
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    for x, y in blocks:
        if graph[x][y] == 0:
            visited[x][y] = 0

    return [cnt, musigae, blocks]

def remove(blocks):
    for x, y in blocks:
        graph[x][y] = -2


def gravity(graph):
    for i in range(n-2, -1, -1):  # 밑에서 부터 체크
        for j in range(n):
            if graph[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<n and graph[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        graph[r+1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break


# 반시계 회전 함수
def rot90(a):
    new_a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i] = a[i][j]
    return new_a

total_score = 0

while True:
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    max_block_cnt = -1
    standard_block = (-1, -1)
    max_musigae = -1
    max_blocks = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                cnt, musigae, blocks = bfs(i, j)
                if cnt >= 2:
                    if cnt > max_block_cnt: # 크기가 가장 큰 블록 그룹
                        max_blocks = blocks
                        max_block_cnt = cnt
                        max_musigae = musigae
                        standard_block = (sorted(max_blocks)[0])
                    elif cnt == max_block_cnt: # 크기가 같은 블록 그룹
                        if musigae > max_musigae: # 무지개 블록의 수가 많은 것
                            max_blocks = blocks
                            max_block_cnt = cnt
                            max_musigae = musigae
                            standard_block = (sorted(max_blocks)[0])
                        elif sorted(max_blocks)[0][0] > standard_block[0] or sorted(max_blocks)[0][1] > standard_block[1]: # 기준 블록의 행이 크거나 열이 큰 것
                            max_blocks = blocks
                            max_block_cnt = cnt
                            max_musigae = musigae
                            standard_block = (sorted(max_blocks)[0])
                    else:
                        continue


    if not max_blocks:
        break

    remove(max_blocks)
    total_score += len(max_blocks) * len(max_blocks)
    gravity(graph)
    rot90(graph)


# print(max_blocks, max_block_cnt, standard_block)
print(total_score)