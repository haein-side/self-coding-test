def solution(n, computers):
    answer = 0

    graph = [[] for _ in range(len(computers))]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    visited = [0 for _ in range(len(graph))]

    def dfs(graph, start_v, visited):
        stack = [start_v]

        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = 1
                for i in graph[v]:
                    stack.append(i)


    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            answer += 1

    return answer


'''
13분 소요
차이점 : graph라는 리스트를 만들어서 갈 수 있는 노드를 넣어주는 인접리스트를 만듦
'''
