t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    if n < m:
        mx = 0
        for j in range(m - n + 1):
            sm = 0
            for i in range(n):
                sm += a_lst[i] * b_lst[i + j]

            if mx < sm:
                mx = sm


    elif n > m:
        mx = 0
        for j in range(n - m + 1):
            sm = 0
            for i in range(m):
                sm += b_lst[i] * a_lst[i + j]

            if mx < sm:
                mx = sm


    else:
        mx = a_lst[i] * b_lst[i]

    print(f'#{tc + 1} {mx}')