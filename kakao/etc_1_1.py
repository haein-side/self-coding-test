from collections import defaultdict
def solution(n, x1, y1, x2, y2):
    answer = []

    rec = []

    for i in range(n):
        rec.append([x1[i], y1[i], x2[i], y2[i]])

    close_rec = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if rec[i][0] == rec[j][2] or rec[i][2] == rec[j][0]:
                if rec[i][1] <= rec[j][3] and rec[i][3] >= rec[j][1]:
                    close_rec[i].append(j)
                    close_rec[j].append(i)
            if rec[i][1] == rec[j][3] or rec[i][3] == rec[j][1]:
                if rec[i][0] <= rec[j][2] and rec[i][2] >= rec[j][0]:
                    close_rec[i].append(j)
                    close_rec[j].append(i)

    # print(close_rec) # [[1], [0, 2], [1], []]

    dic = defaultdict(set) # defaultdict(<class 'set'>, {0: {0, 1, 2}, 1: {0, 1, 2}, 2: {0, 1, 2}, 3: set()})

    for i in range(len(close_rec)):
        for j in close_rec[i]:
            tmp = []
            tmp.extend(close_rec[i])
            tmp.extend(close_rec[j])
            dic[i].update(tmp)
        else:
            dic[i]

    print(dic)

    for i in dic.values():
        if len(i) == 0:
            answer.append(1)
        else:
            answer.append(len(i))

    return answer


print(solution(4, [10,30,65,10], [15,40,40,70], [40,65,80,30], [40,60,70,90]))
