def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(cal, depth, n):
        nonlocal answer
        if depth == n:
            if cal == target:
                answer += 1
                return
            else:
                return

        dfs(cal + numbers[depth], depth + 1, n)
        dfs(cal - numbers[depth], depth + 1, n)


    dfs(0, 0, n)

    return answer