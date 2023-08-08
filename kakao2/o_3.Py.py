from collections import defaultdict
def solution(kor, usa, incs):
    kor_list = [[] for _ in range(len(incs))] # 각 incs에 있는 한국

    for i in range(len(incs)):
        countries = incs[i].split()
        for c in countries:
            if c in kor:
                kor_list[i].append(c)

    usa_dict = defaultdict(dict) # {'AB': {BCD: 0, AAA: 0}}

    for i in range(len(incs)):
        countries = incs[i].split()
        for c in countries:
            if c not in kor_list[i]:
                if c not in usa_dict:
                    usa_dict[c] = dict()
                for j in kor_list[i]:
                    if j not in usa_dict[c].keys():
                        usa_dict[c][j] = 1
                    else:
                        usa_dict[c][j] += 1


    # {'AB': {'BCD': 3, 'AAA': 3, 'AAAAA': 2}, 'AA': {'BCD': 1, 'AAA': 1, 'AAAAA': 2}, 'TTTT': {'BCD': 2, 'AAA': 2, 'AAAAA': 1}})
    # {'XXXX': {}}

    max_value = -1
    for i in usa_dict.keys():
        for k in usa_dict[i].keys():
            if max_value < usa_dict[i][k]:
                max_value = usa_dict[i][k]

    if max_value == -1:
        return 0
    else:
        return max_value


print(solution(["AAA","BCD", "AAAAA", "ZY"], ["AB", "AA", "TTTT"],
               ["AB BCD AA AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"]))
print(solution(["CCC", "BCDF"], ["XXXX"], ["BCDF CCC", "XXXX"]))
