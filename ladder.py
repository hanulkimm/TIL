import sys

sys.stdin = open('input.txt', 'r')

di = [1, 0, 0]  # 아래, 좌 우
dj = [0, -1, 1]


def ldr(i, j):
    for k in range(3):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= i < 100 and 0 <= j < 100 and arr[i][j] == 1:
            i, j = ni, nj


t = int(input())
for tc in range(t):
    arr = [list(map(int, input().split())) for _ in range(100)]

    i = 0
    for j in range(100):
        if i == 100:
            print(True)
        else:
            ldr(i, j)




