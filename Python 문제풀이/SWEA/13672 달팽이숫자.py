import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    di = [0, 1, 0, -1] # 오른쪽에서 출발해서 시계 방향
    dj = [1, 0, -1, 0]
    i = j = dr = 0  # 초기 설정

    for cnt in range(1, n**2+1):
        arr[i][j] = cnt
        ni, nj = i + di[dr], j + dj[dr]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dr = (dr+1) % 4  # 0 1 2 3 0 1 2 3....
            i, j = i + di[dr], j + dj[dr]
    print(f'#{tc+1}')

    for lst in arr:
        print(*lst)
