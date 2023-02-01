import sys
sys.stdin = open('input.txt','r')

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    mx = 0
    mn = 10000 * m

    for i in range(n-m+1):
        sm = 0
        for j in range(m):
            sm += lst[i+j]

        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm

    print(f'#{tc+1} {mx-mn}')

    # print(mx, mn)

