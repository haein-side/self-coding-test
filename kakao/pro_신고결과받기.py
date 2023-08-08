from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    reported_num = defaultdict(int) # {muzi : 0}
    reporter = defaultdict(list) # {muzi : ["frodo", "neo"]}
    for i in id_list:
        reported_num[i] = 0
        reporter[i] = []

    for i in report:
        a, b = i.split()
        if b not in reporter[a]:
            reporter[a].append(b)
            reported_num[b] += 1

    for value in reporter.values():
        tmp = 0
        for v in value:
            if reported_num[v] >= k:
                tmp += 1
        answer.append(tmp)

    return answer
