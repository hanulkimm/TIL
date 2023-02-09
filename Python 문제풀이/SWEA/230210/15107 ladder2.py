import sys
from copy import deepcopy

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    t = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    ci = 99
    lst_j = []
    for j in range(102):
        if arr[ci][j] == 1:
            lst_j.append(j)

    mn = 100 * 100

    mn = 10000
    ans = 0
    for k in lst_j:
        arr1 = deepcopy(arr)
        ci = 99
        cnt = 0
        cj = k

        while ci > 0:
            arr1[ci][cj] = 0
            if arr1[ci][cj - 1] == 1:
                cj -= 1
                cnt += 1
            elif arr1[ci][cj + 1] == 1:
                cj += 1
                cnt += 1
            else:
                ci -= 1
                cnt += 1
        if mn > cnt:
            mn = cnt
            ans = cj
    print(f'#{tc+1} {ans-1}')

