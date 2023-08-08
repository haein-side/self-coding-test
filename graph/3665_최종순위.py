import sys
input = sys.stdin.readline

n = int(input())

'''
언급되지 않은 거는 순서가 바뀌면 안된다!

사이클이 존재한다면 IMPOSSIBLE 출력
- 진입차수가 0인 노드가 없어 시작노드가 없을 때
- 위상 정렬을 끝냈는 데도 방문하지 않은 정점이 있을 때

불확실한 경우 생기지 않음 <- 모든 노드의 상대적인 위치를 알고 있으므로 (같은 위상에 있는 게 없으므로)

https://hongcoding.tistory.com/96
'''

from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    queue = deque()
    answer = []
    flag = 0

    team = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            inDegree[team[k]] += 1

    m = int(sys.stdin.readline())
    for j in range(m):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        flag = True

        for k in graph[first]:
            if k == second:
                graph[first].remove(second)
                inDegree[second] -= 1
                graph[second].append(first)
                inDegree[first] += 1
                flag = False

        if flag:
            graph[second].remove(first)
            inDegree[first] -= 1
            graph[first].append(second)
            inDegree[second] += 1

    for j in range(1, n + 1):
        if inDegree[j] == 0:
            queue.append(j)

    if not queue:
        print("IMPOSSIBLE")
        continue

    result = True
    while queue:
        if len(queue) > 1:
            result = False
            break

        tmp = queue.popleft()
        answer.append(tmp)
        for j in graph[tmp]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                queue.append(j)
            elif inDegree[j] < 0:
                result = False
                break

    if not result or len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
