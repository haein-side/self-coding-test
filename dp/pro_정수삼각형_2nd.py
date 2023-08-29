def solution(triangle):
    answer = 0

    dp = [[] for _ in range(len(triangle))]

    for i in range(len(triangle)):
        dp[i] = [0 for i in range(i+1)]

    n = len(triangle)

    for i in range(n):
        dp[n-1][i] = triangle[n-1][i]

    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            dp[i][j] = max(dp[i+1][j] + triangle[i][j],
                           dp[i+1][j+1] + triangle[i][j])
    answer = dp[0][0]
    return answer
