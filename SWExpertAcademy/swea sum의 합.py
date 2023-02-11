import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    mx = 0

    for i in range(100):
        sm_1 = 0
        sm_2 = 0
        for j in range(100):
            sm_1 += arr[i][j]
            sm_2 += arr[j][i]

        if mx < sm_1:
            mx = sm_1
        if mx < sm_2:
            mx = sm_2

    sm3 = 0
    sm4 = 4
    for i in range(100):
        sm3 += arr[i][i]
        sm4 += arr[i][99-i]

        if mx < sm3:
            mx = sm3
        if mx < sm4:
            mx = sm4

    print(f'#{tc+1} {mx}')