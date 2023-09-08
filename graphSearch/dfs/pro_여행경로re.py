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

    print(destinations)

    def dfs(v):
        if len(visited) == len(tickets):
            return tmp_answer

        for a, b in destinations[v]:
            if b not in visited: # 티켓 번호가 들어있지 않으면
                visited.append(b) # 티켓 사용
                tmp_answer.append(a) # 경로 추가
                returned_result = dfs(a)

                print("r", returned_result)

                if returned_result is not None:  # dfs 재귀 후 돌아왔을 때 리턴 값이 None이 아니라 뭐라도 존재하면 16라인에서 걸려서 리턴값이 존재하는 것임! -> 즉 모든 티켓을 다 사용했다는 뜻!!
                    return returned_result
                else: # 재귀호출 후 더이상 진행할 수 없을 때 파이썬에선 None이 반환됨!
                    print(visited, tmp_answer)
                    visited.pop()
                    tmp_answer.pop()


    tmp_answer.append('ICN')
    answer = dfs('ICN')

    return answer

solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])

'''
2/23 다시 풀어 보기...
1. visited 처리
visited 처리를 해주기 위해 visit 한 ticket num을 담아서 관리하는 리스트 만들고 그 안에 ticket num이 있는지 없는지 확인하는 방식

2. visited 처리를 어디서 해주는지도 매우 중요
for문을 돌면서 그 안에서 인접한 노드들의 visited 처리를 해주어야 ticket_num을 그 자리에서 visited 리스트에 넣어줄 수 있음 
이렇게 한 이유는 dfs() 인천 함수를 처음 호출할 때 안 그러면 신경 써줘야 하는 것들이 꽤 있음..
'''

'''
9/9 다시 복습하기...
만약에 A에서 더이상 if b not in visited를 충족 못해서 
재귀 호출에서 더 이상 진행할 수 없는 경우에 무엇을 리턴하는지 아는 것이 매우 중요함
일반적으로 재귀 호출에서 더이상 진행 불가능 경우에 None을 반환

따라서 28번 라인에서 returned_result에서 

if returned_result를 했는데
이런 경우는 해당 변수가 None이 아니면서 다른 falsy한 값들 (0, 빈 문자열, 빈 리스트 등)이 아닌 경우에만 조건이 참이 됩니다. 
따라서 변수가 None인지 확인하려면 if returned_result를 is None:과 같이 명시적으로 is None을 사용하는 것이 더 정확하고 안전하다.
'''
