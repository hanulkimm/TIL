import sys

sys.stdin = open('input.txt', 'r')

t = int(input())


for tc in range(t):
    lst = list(range(1, 13))
    ans= 0
    n, k = map(int, input().split())

    for bit in range(1<<12):
        sm = 0
        cnt = 0
        for j in range(12):
            if bit & (1<<j):
                sm += lst[j]
                cnt += 1

        if sm == k and cnt == n:
            ans += 1

    print(f'#{tc+1} {ans}')

