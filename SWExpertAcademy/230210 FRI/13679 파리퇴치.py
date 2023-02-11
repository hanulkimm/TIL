import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sm = 0
            for k in range(m):
                for l in range(m):
                    sm += arr[i+k][j+l]
                if ans < sm:
                    ans = sm
    print(f'#{tc+1} {ans}')
