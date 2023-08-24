import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())


def bfs(start_v):
    queue = deque([start_v])
    visited = [0 for _ in range(f + 1)]
    visited[start_v] = 1
    answer = 0
    flag = False

    while queue:
        v = queue.popleft()

        if v == g:
            flag = True
            break
        else:
            if v > g and f >= v - d >= 1 and not visited[v - d]:
                answer += 1
                v -= d
                visited[v] = 1
                queue.append(v)
            elif v <= g and 1 <= v + u <= f and not visited[v + u]:
                answer += 1
                v += u
                visited[v] = 1
                queue.append(v)
            elif v <= g and v + u > f >= v - d >= 1 and not visited[v - d]:
                answer += 1
                v -= d
                visited[v] = 1
                queue.append(v)
            elif v > g and v - d < 1 <= v + u <= f and not visited[v + u]:
                answer += 1
                v += u
                visited[v] = 1
                queue.append(v)

    return [answer, flag]


if s == g:
    print(0)
else:
    result, isTrue = bfs(s)
    if not isTrue:
        print("use the stairs")
    else:
        print(result)
