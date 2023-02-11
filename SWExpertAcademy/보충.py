import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)

    mx = 0
    sm = 0
    for i in range(n):
        for j in range(n):
            for di, dj in ((0,0), (1, 0),  (0, 1), (1,1)):
                ni, nj = i + di, j + dj

            if 0<=ni<n and 0<=nj<nj:
                sm += arr[ni][nj]

            if mx < sm:
                mx = sm
    print(mx)

