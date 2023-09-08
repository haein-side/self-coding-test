from collections import defaultdict


def solution(tickets):
    t_dict = defaultdict(list)

    # key: 출발지, value: 목적지인 딕셔너리 만듦
    for s, e in tickets:
        t_dict[s].append(e)

    # 목적지 기준 내림차순 정렬(맨 오른쪽걸 pop해서 쓸거임. 알파벳 순서 상 가장 앞선 것)
    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse=True)

    print(t_dict)
    answer = []
    path = ["ICN"]

    # DFS를 실행함. 처음에는 맨 마지막 공항까지 쭉쭉 나아감.
    # 어느 순간 다른 공항으로 가는 티켓도 없고, 또는 그런 티켓을 다 소진한
    # 어떤 공항에 도착한다면 그 곳이 맨 마지막에 도달하게 될 공항임.
    # 이제 path에서 pop해서 하나씩 answer에 넣어줌으로써 path를 역방향으로
    # 거슬러 올라갈거임. 다만 맨 마지막 공항에 처음으로 도착했을 때의 path
    # 가 모든 간선을 다 사용하지 않은 path일 수도 있음. 그러므로, 한 칸씩
    # 내려가면서 그 공항과 연결된 인접 공항들을 싹 다 돌아주면 됨.
    # 이렇게 ICN까지 쭉 실행해주면 path는 비게 되고 answer에는 역방향의 정답
    # 루트가 담겨있게 됨.

    # t_dict {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']})
    while path:
        now = path[-1]
        print(":::: now " + now)

        # t_dict에 now라는 key가 있는지 없는지 확인
        if now not in t_dict or len(t_dict[now]) == 0:
            print(":::: t_dict " , t_dict , " :::: now " , now)
            answer.append(path.pop())
            print(":::: answer " , answer)
        else:
            path.append(t_dict[now].pop())
            print(":::: path " , path)

    return answer[::-1]


solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])
