import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 0

    while q:
        si, sj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < n:
                tmp = v[si][sj] + 1
                if arr[ni][nj] > arr[si][sj]:
                    tmp += (arr[ni][nj] - arr[si][sj])
                if v[ni][nj] > tmp:
                    v[ni][nj] = tmp
                    q.append((ni, nj))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    INF = 1e9
    v = [[INF] * n for _ in range(n)]
    bfs(0, 0)
    ans = v[n - 1][n - 1]
    print(f'#{tc} {ans}')
