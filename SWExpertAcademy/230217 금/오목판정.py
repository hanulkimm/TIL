import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    ans = 'NO'

    for _ in range(2): # arr 와  arr_transpose
        for i in range(n):
            sm = 0
            j = 0
            while j < n:
                if arr[i][j] == 'o':
                    sm += 1
                else:
                    sm= 0 # 연속하지 않는 경우
                j += 1
                if sm >= 5:
                    ans = 'YES'
                    break
            if sm >= 5: # 마지막까지 돌고 나서 다시 확인해주기
                ans = 'YES'
        arr = list(zip(*arr))

    sm2 = sm3 = 0
    for i in range(n):
        if arr[i][i] == 'o':
            sm2 += 1
        if arr[i][i] == '.':
            sm2 = 0
        if arr[i][n-1-i] == 'o':
            sm3 += 1
        else:
            sm3 = 0

        if sm2 >= 5 or sm3 >= 5:
            ans = 'YES'
            break
    print(f'#{tc} {ans}')