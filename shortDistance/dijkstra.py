import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) # 최단 거리 테이블 : 처음 초기화 땐 INF

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a번->b번 비용 c


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # (정점까지 최단거리, 정점)
    distance[start] = 0 # 최단 거리 테이블 : 자기자신 -> 자기자신까지의 거리는 0

    while q:
        # 2. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
        # now점까지 거리, now정점
        # 큐에 있는 게 항상 최단 거리는 X 갱신된 거리 정보가 노드와 함께 들어가 있는 것 (갱신된 기록)
        # 다른 노드를 통해 가는 게 더 최소 거리일 수도 있음
        dist, now = heapq.heappop(q)

        # 현재까지의 최단거리 < now점까지 거리
        # 여러 간선 중 이미 최단 거리인 점보다 긴 간선 발견 시 continue
        # 만약 > 라면, dist가 최단 거리가 아닌 것
        if distance[now] < dist:
            continue

        # dist가 최단 거리인 것
        for i in graph[now]:
            cost = dist + i[1] # dist: 지금까지 최단 거리 + i[1]: 인접 점까지 거리
            if cost < distance[i[0]]: # i[0]: 인접 점, 만약 최단 거리 테이블보다 작으면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성
                print(q)


# 1. 출발 노드 설정
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
