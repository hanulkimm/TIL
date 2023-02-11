import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    mn_i = n
    mn_j = n
    mx_i = 0
    mx_j = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] =='#':
                if mn_i > i:
                    mn_i = i
                if mn_j > j:
                    mn_j = j
                if mx_i < i:
                    mx_i = i
                if mx_j < j:
                    mx_j = j

    ans = 'yes'
    if mx_i-mn_i != mx_j-mn_j: #가로, 세로 길이가 같지 않는 경우
        ans = 'no'

    for i in range(mx_i-mn_i+1):
        for j in range(mx_j-mn_j+1):
            if arr[mn_i+i][mn_j+j] != '#': # 정사각형 안이 안 채워져 있는 경우
                ans = 'no'

    print(f'#{tc+1} {ans}')
