from collections import deque
def bfs(place):
    start = [] # p인 점들

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i, j)) # i : y, j : x

    for y, x in start:
        queue = deque()
        queue.append((y, x))
        visited = [[0 for _ in range(5)] for _ in range(5)] # 5 * 5
        distance = [[0 for _ in range(5)] for _ in range(5)]
        visited[y][x] = 1

        while queue:
            cy, cx = queue.popleft()

            mx, my = [1, 0, -1, 0], [0, -1, 0, 1]

            for i in range(4):
                ny, nx = cy + my[i], cx + mx[i]

                if 0 <= ny <= 4 and 0 <= nx <= 4 and visited[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        distance[ny][nx] = distance[cy][cx] + 1 # 이 부분에서 실수했었음 - 누적
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                    elif distance[cy][cx] <= 1 and place[ny][nx] == 'P':
                        return False
    return True

def solution(places):
    answer = []

    for p in places:
        if bfs(p) : # return True -> 거리두기 지킴
            answer.append(1)
        else:
            answer.append(0)

    return answer
