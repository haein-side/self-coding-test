from collections import deque

# 인접 블록 찾기 -> 블록 크기, 무지개 크기, 블록좌표 리턴
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    block_cnt, rainbow_cnt = 1, 0
    visited_blocks, rainbows = [[x, y]], []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + mv[d]
            ny = y + mv[d]

            # 범위 안이면서 방문 안 한 일반 블록의 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = 1
                q.append([nx, ny])
                block_cnt += 1
                visited_blocks.append([nx, ny])

            # 범위 안이면서 방문 안 한 무지개 블록인 경우
            elif 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                graph.append([nx, ny])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([nx, ny])

    # 무지개 블록은 방문 다시 해제
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, visited_blocks + rainbows]

# 블록 제거 함수
def remove(block):
    for x, y in block:
        graph[x][y] = -2

# 중력 함수
def gravity(graph):
    for i in range(n-2, -1, -1):
        for j in range(n):
            if graph[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and graph[r+1][j] == -2:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break

# 반시계 회전 함수
def rot90(a):
    new_a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i] = a[i][j]

    return new_a


# 0. 메인코드
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

score = 0

# 1. 오토플레이 -> while {2. 크기가 가장 큰 블록 찾기, 3. 블록 제거 + 점수 더하기 4. 중력 5. 90도 회전 6. 중력}
while True:
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    blocks = [] # 가능한 블록 그룹들 넣을 리스트

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]: # 일반 블록이면서 방문 안 했으면
                visited[i][j] = 1
                block_info = bfs(i, j, graph[i][j]) # 인접한 블록 찾기 [블록 크기, 무지개 블록 개수, 블록 좌표]
                if block_info[0] >= 2:
                    blocks.append(block_info)

    blocks.sort(reverse=True) # 블록 크기가 제일 큰 블록 그룹부터 정렬

    # 3. 블록 제거 + 점수 더하기
    if not blocks:
        break

    remove(blocks[0][2]) # 블록 좌표 리스트
    score += blocks[0][0] ** 2 # 블록 크기의 제곱 더하기

    # 4. 중력
    gravity(graph)

    # 5. 90도 회전
    graph = rot90(graph)

    # 6. 중력
    gravity(graph)


print(score)
