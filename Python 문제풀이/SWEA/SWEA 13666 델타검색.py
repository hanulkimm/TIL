import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sm = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if arr[i][j]-arr[ni][nj] >= 0:
                        sm += arr[i][j]-arr[ni][nj]
                    else:
                        sm += arr[ni][nj] - arr[i][j]

    print(f'#{tc+1} {sm}')



