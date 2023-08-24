from collections import defaultdict
def solution(tickets):
    answer = []
    destinations = defaultdict(list)
    tickets.sort(key = lambda x : (x[0], x[1]))
    ticket_num = 0
    visited, tmp_answer = [], []
    # 방문 시 리스트 안에 ticket_num 있는지 보고 없으면 append 해주는 visited 리스트
    # 방문 기록을 남기는 tmp_answer 리스트

    for a, b in tickets:
        ticket_num += 1
        destinations[a].append((b, ticket_num))

    def dfs(v):
        if len(visited) == len(tickets):
            return tmp_answer

        for a, b in destinations[v]:
            if b not in visited:
                visited.append(b)
                tmp_answer.append(a)
                returned_result = dfs(a)

                if returned_result:  # dfs 재귀 후 돌아왔을 때 리턴 값이 None이 아니라 뭐라도 존재하면 16라인에서 걸려서 리턴값이 존재하는 것임! -> 즉 모든 티켓을 다 사용했다는 뜻!!
                    return returned_result
                else:
                    visited.pop()
                    tmp_answer.pop()


    tmp_answer.append('ICN')
    answer = dfs('ICN')

    return answer

'''
2/23 다시 풀어 보기...
1. visited 처리
visited 처리를 해주기 위해 visit 한 ticket num을 담아서 관리하는 리스트 만들고 그 안에 ticket num이 있는지 없는지 확인하는 방식

2. visited 처리를 어디서 해주는지도 매우 중요
for문을 돌면서 그 안에서 인접한 노드들의 visited 처리를 해주어야 ticket_num을 그 자리에서 visited 리스트에 넣어줄 수 있음 
이렇게 한 이유는 dfs() 인천 함수를 처음 호출할 때 안 그러면 신경 써줘야 하는 것들이 꽤 있음..
'''
