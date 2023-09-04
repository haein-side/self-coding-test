from collections import deque

def solution(begin, target, words):
    answer = -1

    # words안에 target 없는 케이스
    if target not in words:
        return 0

    def bfs(start_v):
        queue = deque([start_v])
        visited = dict()

        for i in words:
            visited[i] = 0

        visited[start_v] = 1

        while queue:
            w = queue.popleft()

            if w == target:
                return visited[target] - 1

            for s in words:
                tmp = len(w)
                for k in range(len(w)):
                    if s[k] == w[k]:
                        tmp -= 1
                if tmp == 1 and visited[s] == 0:
                    queue.append(s)
                    visited[s] = visited[w] + 1

    answer = bfs(begin)

    if answer:
        return answer
    else:
        return 0


