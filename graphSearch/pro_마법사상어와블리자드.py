N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]


n2loc = {} # 번호 -> 좌표
loc2n = {} # 좌표 -> 번호
n2ball = [-1] * N**2 # 번호 -> 번호에 이해당하는 공 번호
result = 0

def init_grid():
    """
    2차원 좌표 정보를 1차원으로 변경
    :return:
    """
    global n2loc, loc2n

    # 우 하 좌 상
    dy_temp = (0, 1, 0, -1)
    dx_temp = (1, 0, -1, 0)

    loc = (0, -1) # 시작을 (0, -1)로 해서 (0, 0)에서 부터 시작하도록
    cnt = N ** 2 - 1 #  마지막 번호 = N^2-1
    dist, dist_change_flag = N, 1 # 처음 이동거리 N, 이동거리 변화 Flag
    dir = 0

    while True:
        for i in range(dist):
            ny = loc[0] + dy_temp[dir]
            nx = loc[1] + dx_temp[dir]

            loc = (ny, nx) # 좌표 갱신
            n2loc[cnt] = (ny, nx)  # 번호 -> 좌표
            loc2n[(ny, nx)] = cnt # 좌표 -> 번호
            n2ball[cnt] = board[ny][nx] # 번호 -> 구슬 번호
            cnt -= 1

        dir = (dir + 1) % 4 # 방향 번경
        dist_change_flag += 1
        if dist_change_flag == 2: # 방향을 2번 변경하면 dist 1 감소
            dist_change_flag = 0
            dist -= 1

        if dist == 0: break # 거리가 0이 되면 종료
