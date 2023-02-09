import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_90 = [[0] * n for _ in range(n)]
    arr_180 = [[0] * n for _ in range(n)]
    arr_270 = [[0] * n for _ in range(n)]

    # 90도 회전
    for j in range(n):
        for i in range(n):
            arr_90[j][i] = arr[n-i-1][j]
    # 180도 회전
    for j in range(n):
        for i in range(n):
            arr_180[j][i] = arr_90[n-i-1][j]
    # 270도 회전
    for j in range(n):
        for i in range(n):
            arr_270[j][i] = arr_180[n-i-1][j]

    print(f'#{tc+1}')
    for i in range(n):
        print(*arr_90[i] ,' ', *arr_180[i], ' ', *arr_270[i] , sep='')
