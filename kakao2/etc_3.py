from bisect import bisect_left

def max_people_in_range(A, n, k, a, b):
    # A: 사람들의 위치 정보
    # n: 사람의 수
    # k: 각 사람이 이동할 수 있는 최대 거리
    # a, b: 구간의 최소, 최대 값

    left = [max(A[i] - k, a) for i in range(n)]
    right = [min(A[i] + k, b) for i in range(n)]

    print(left, right)

    # 슬라이딩 윈도우를 이용하여 최대 인원 수 찾기
    max_people = 0
    i = j = 0
    while i < n and j < n:
        # 현재 윈도우 안에 포함된 사람 수 계산
        count = j - i + 1
        # 윈도우를 오른쪽으로 이동시킬 수 있는 경우
        if j + 1 < n and right[j + 1] >= left[i]:
            j += 1
        # 윈도우를 왼쪽으로 이동시킬 수 있는 경우
        elif i + 1 < n and left[i + 1] <= right[j]:
            i += 1
        # 윈도우를 이동시킬 수 없는 경우
        else:
            i += 1

        # 현재 구간 안에 최대한 많은 사람이 포함될 수 있도록
        # 슬라이딩 윈도우의 크기를 조절
        while j + 1 < n and right[j + 1] >= left[i]:
            j += 1
            count += 1

        # 최대 인원 수 갱신
        max_people = max(max_people, count)

    return max_people


print(max_people_in_range([1, 2, 1, 2], 4, 1, 1, 4))
