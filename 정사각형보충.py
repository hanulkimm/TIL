import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [ list(input()) for _ in range(n)]

    mn_i = n
    mn_j = n
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                si, sj = i, j
                if mn_i > si:
                    mn_i = si
                if mn_j > sj:
                    mn_j = sj

    si = mn_i
    sj = mn_j

    ej = sj
    stp = 0
    for k in range(sj+1, n):
        if arr[si][k] != '#':
            stp = -1
            break
        elif arr[si][k] == '#':
            ej += 1

    cnt = 0
    dif = ej - sj #1
    for i in range(si, si+dif+1):
        for j in range(sj, sj+dif+1):
            if arr[i][j] == '#':
                cnt += 1

    if cnt == (ej-sj+1)**2 and stp != -1:
        print(f'#{tc+1} yes')
    else:
        print(f'#{tc+1} no')

