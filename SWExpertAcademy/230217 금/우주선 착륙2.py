import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [-1, 1, 0, 0, -1, 1, 1, -1] # 상 하 좌 우 # 다음에 대각선들
    dj = [0, 0, -1, 1, 1, 1, -1, -1]

    ans = 0
    for i in range(n):
        for j in range(m):
            sm= 0
            for k in range(8):
                ni, nj = i + di[k], j + dj[k]
                if 0<=ni<n and 0<=nj<m and arr[ni][nj] < arr[i][j]:
                    sm += 1
            if sm >= 4:
                ans += 1
    print(f'#{tc} {ans}')

