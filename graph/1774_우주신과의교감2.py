import sys
import math
input = sys.stdin.readline

'''
1. 이미 연결된 통로는 union을 통해서 이어줌 -> 하나의 그룹으로 묶음
2. 모든 노드들에 대해 연결 가능한 조합을 해당 조합의 거리와 함께 possible 리스트에 담아줌
3. 거리를 기준으로 오름차순 정리
4. 크루스칼 알고리즘을 사용해 연결
5. 새로 연결되는 선분의 거리를 ans에 더해줌
이미 연결된 통로는 union을 통해서 연결했기 때문에 다시 선택되는 경우는 없음
'''
def find(parent, x):
    if x != parent[x]: # 루트 노드가 아니라면
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

space = [0 for _ in range(n+1)] # 우주신 좌표 (x, y) 1, n번째 인덱스로 수정함
for i in range(1, n+1):
    x, y = map(int, input().split())
    space[i] = (x, y) # 수정함

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b) # 이미 연결된 통로는 Union을 통해서 이어줌 -> 하나의 그룹으로 묶음

# 모든 노드들에 대해 연결 가능한 조합을 거리와 함께 리스트에 담아줌
possible = [] # (dist, a, b)
for i in range(1, len(space)-1): # n-1
    for j in range(i+1, len(space)): # n
        x1, x2, y1, y2 = space[i][0], space[j][0], space[i][1], space[j][1]
        dist = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
        possible.append((dist, i, j))

possible.sort()
result = 0
# 크루스칼 알고리즘을 통해 연결 <- 서로 루트 노드가 같지 않을 때만 하나의 집합으로 union해줌 -> 즉 "하나의 경로 // 연결" 시켜줌!
# find()로 루트 노드를 찾아주고, 루트노드가 같지 않을 때 연결되어 있지 않은 것이므로 Union()으로 연결시켜주는 것
for dist, i, j in possible:
    if find(parent, i) != find(parent, j):
        union(parent, i, j)
        result += dist

print("{:.2f}".format(result))
