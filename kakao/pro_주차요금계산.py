from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    total_time = defaultdict(list)

    for i in range(len(records)):
        a, b, c = records[i].split()
        hour, minute = map(int, a.split(":"))
        time = hour * 60 + minute
        total_time[b].append(time)

    time_dict = defaultdict(int) # {'5961': 146, '0000': 334, '0148': 670}

    for i in total_time:
        if len(total_time[i]) % 2 != 0:
            total_time[i].append(1439)

        time_dict[i] = 0
        for j in range(len(total_time[i])-1, 0, -2):
            time_dict[i] += (total_time[i][j] - total_time[i][j-1])

    sorted_dict = sorted(time_dict.items(), key = lambda x:x[0])

    basic_time, basic_fee, time_loop, fee_loop = fees[0], fees[1], fees[2], fees[3]

    for c, t in sorted_dict:
        if t <= basic_time:
            answer.append(basic_fee)
        else:
            t -= basic_time
            answer.append(math.ceil(t / time_loop) * fee_loop + basic_fee)

    return answer
