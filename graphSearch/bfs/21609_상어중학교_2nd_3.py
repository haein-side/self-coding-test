def gravity():
    global blocks
    temp = 0
    for c in range(N):
        for r in range(N - 1, -1, -1):
            # 아래 블록
            cur_r = r
            while cur_r > 0 and blocks[cur_r][c] == -2:
                cur_r -= 1
            if cur_r != r and blocks[cur_r][c] != -1:
                temp = blocks[cur_r][c]
                blocks[cur_r][c] = -2
                blocks[r][c] = temp

    return


def rotate():
    global blocks
    temp_blocks = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp_blocks[r][c] = blocks[c][N - 1 - r]

    blocks = temp_blocks[:]
    return

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N, M = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

score = 0
while True:
    # 1. 가장 큰 블록 그룹 찾기
    largest_block = list()
    largest_rainbow = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 1:
                continue
            cur_block = blocks[r][c]
            if cur_block <= 0:
                continue
            visited[r][c] = 1
            result_list = [[r, c]]
            queue = [[r, c]]
            rainbow_num = 0
            while queue:
                qr, qc = queue.pop(0)
                for i in range(4):
                    cr = qr + dr[i]
                    cc = qc + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and visited[cr][cc] == 0 and (
                            blocks[cr][cc] == 0 or blocks[cr][cc] == cur_block):
                        result_list.append([cr, cc])
                        visited[cr][cc] = 1
                        if blocks[cr][cc] == 0:
                            rainbow_num += 1
                            visited[cr][cc] = 2

                        if len(largest_block) < len(result_list):
                            largest_block = result_list[:]
                            largest_rainbow = rainbow_num
                        elif len(largest_block) == len(result_list) and largest_rainbow <= rainbow_num:
                            largest_block = result_list[:]
                            largest_rainbow = rainbow_num
                        queue.append([cr, cc])
            # 무지개 visited 초기화
            for tr in range(N):
                for tc in range(N):
                    if visited[tr][tc] == 2:
                        visited[tr][tc] = 0

    # 1-1 block 갯수가 1 이하면 break
    if len(largest_block) <= 1:
        break
    else:
        score += len(largest_block) ** 2

    # 2. 찾은 블록들 제거하기
    for tr, tc in largest_block:
        blocks[tr][tc] = -2

    # 3. 중력
    gravity()

    # 4. 반시계 90도
    rotate()

    # 5. 중력
    gravity()

print(score)