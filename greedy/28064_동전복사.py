'''
cases

1 - 기계의 한 변의 길이가 1일 때 작동 횟수 0
2 - 동전의 위치가 꼭짓점일 때
3 - 동전의 위치가 꼭짓점을 제외하고 테두리에 있을 때
4 - 동전의 위치가 꼭짓점이 아닐 때
'''
import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())

if n == 1:
    print(0)
elif (x, y) in [(1, 1), (n, n), (1, n), (n, 1)]:
    print(2)
elif y == 1 or y == n or x == 1 or x == n:
    print(3)
else:
    print(4)

