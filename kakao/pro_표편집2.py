def solution(n, k, cmds):
    linked_list = {i: [i-1, i+1] for i in range(n)} # -1 prev이면 맨 첫번째, n post이면 마지막번째라는 것
    table = ['O'] * n
    delete = []

    for cmd in cmds:
        cmd = cmd.split() # 문자열이 한 개이더라도 Split 가능함

        if cmd[0] == 'D':
            for _ in range(int(cmd[1])): # X번만큼 post 이동
                k = linked_list[k][1]

        elif cmd[0] == 'U':
            for _ in range(int(cmd[1])): # X번만큼 prev 이동
                k = linked_list[k][0]

        elif cmd[0] == 'C':
            prev, nxt = linked_list[k]
            table[k] = 'X'
            delete.append((prev, k, nxt))

            if nxt == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == -1: # 맨 처음 숫자이면
                linked_list[nxt][0] = prev
            elif nxt == n : # 마지막 숫자이면
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev

        else:
            prev, now, post = delete.pop()
            table[now] = 'O'

            if prev == -1:
                linked_list[post][0] = now
            elif post == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[post][0] = now


    return "".join([x for x in table])
