import sys

sys.stdin = open('input.txt', 'r')


n = int(input())
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

print(mx)