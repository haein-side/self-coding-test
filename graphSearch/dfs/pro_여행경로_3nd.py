from collections import defaultdict
def solution(tickets):
    answer = []
    tickets.sort()
    tick = defaultdict(list)
    ticket_num = 0
    for a, b in tickets:
        ticket_num += 1
        tick[a].append((b, ticket_num))

    used_tickets = []
    path = ['ICN']

    def dfs(v):

        if len(used_tickets) == ticket_num:
            return path

        for a, b in tick[v]:
            if b not in used_tickets:
                path.append(a)
                used_tickets.append(b)
                tmp = dfs(a)

                if tmp is not None:
                    return path
                else:
                    path.pop()
                    used_tickets.pop()

    answer = dfs('ICN')
    return answer
