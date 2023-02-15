import sys
sys.stdin = open('input.txt', 'r')
#
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # arr 는 1(벽)으로 둘러싸기
    arr = [[1] * (n+2)] + [[1]+ list(map(int, input()))+[1] for _ in range(n)] + [[1] * (n+2)]

    si, sj = 0, 0
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] == 2:
                si, sj = i, j


    stk = []
    i, j = si, sj
    ans = 0

    while True:
        arr[i][j] = 1 # 한 번 지나가면 벽으로 바꾸기
        if arr[i][j-1] == 3 or arr[i][j+1] == 3 or arr[i-1][j]==3 or arr[i+1][j]==3:
            ans = 1
            break
        elif arr[i][j-1] == 0 : # 좌
            dr = 0
            stk.append([i,j,dr])
            i, j = i, j-1

        elif arr[i][j+1] == 0: # 우
            dr = 1
            stk.append([i,j,dr])
            i, j = i, j+1

        elif arr[i-1][j] == 0 : # 상
            dr = 2
            stk.append([i,j,dr])
            i, j = i-1, j

        elif arr[i+1][j] == 0 : # 하
            dr = 3
            stk.append([i,j,dr])
            i, j = i+1, j
        else:
            if stk: # 돌아갈 길이 있다면
                i, j, dr = stk.pop()
            else: #없다면(정답까지 도착하는 길이 없음)
                ans = 0
                break

    print(f'#{tc} {ans}')
