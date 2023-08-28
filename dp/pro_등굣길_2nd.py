def solution(m, n, puddles):
    answer = 0

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for x, y in puddles:
        dp[y][x] = "x"

    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            else:
                if dp[i][j] == 'x':
                    dp[i][j] = 0
                else:
                    if dp[i-1][j] == 0 and dp[i][j-1] == 0:
                        dp[i][j] = 0
                    elif dp[i-1][j] != 0 and dp[i][j-1] == 0:
                        dp[i][j] = dp[i-1][j]
                    elif dp[i-1][j] == 0 and dp[i][j-1] != 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[n][m]

    return answer % 1000000007
