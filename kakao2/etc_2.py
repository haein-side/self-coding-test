# import bisect
# def sliding_window(A, n, k, a, b):
#     # A 배열을 정렬합니다.
#     A.sort()
#
#     # 윈도우 내에 있는 사람들 중에서 범위 [a, b]에 속하는 사람들을 찾습니다.
#     def count_people_in_range(start, end):
#         left = bisect.bisect_left(A, start)
#         right = bisect.bisect_right(A, end)
#         return right - left
#
#     # 슬라이딩 윈도우를 이용하여 범위 [a, b]에 속하는 사람들의 최대 개수를 찾습니다.
#     ans = 0
#     left = 0
#     right = 0
#     while right < n:
#         # 윈도우 내에 있는 사람들 중에서 범위 [a, b]에 속하는 사람들의 개수를 구합니다.
#         cnt = count_people_in_range(a - A[right], b - A[right])
#
#         # 범위 [a, b]에 속하는 사람들의 개수가 현재 최대값보다 크면 갱신합니다.
#         ans = max(ans, cnt)
#
#         # 윈도우를 오른쪽으로 이동합니다.
#         right += 1
#
#         # 윈도우의 크기가 k를 초과하면 윈도우를 왼쪽으로 이동합니다.
#         if right - left > k:
#             left += 1
#
#     return ans

def max_people_in_range(n, A, k, a, b):
    # A를 오름차순으로 정렬
    A.sort()

    # 각 사람이 이동할 수 있는 구간 계산
    left = [max(A[i]-k, a) for i in range(n)]
    right = [min(A[i]+k, b) for i in range(n)]

    # dp 배열 초기화
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        # i번째 사람을 선택하지 않은 경우
        count = 0
        for j in range(i):
            if left[i] <= A[j] <= right[i]:
                count += 1
        dp[i] = count

        # i번째 사람을 선택한 경우
        for j in range(i-1, -1, -1):
            if right[j] < left[i]:
                break
            if left[i] <= A[j] <= right[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return dp[n-1]

print(max_people_in_range(4, [1, 2, 1, 2], 1, 1, 4))
