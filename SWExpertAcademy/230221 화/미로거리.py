import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                si, sj = i, j

    v = [[0] * n for _ in range(n)]
    v[si][sj] = 1
    q = []
    q.append((si, sj))
    flag = 0
    ans = 0
    while q:
        if flag == 1:
            break
        i, j = q.pop(0)
        for di, dj in ((-1,0), (1, 0), (0, -1), (0, 1)): # 상하좌우
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 : # 범위 내이고 미방문
                if arr[ni][nj]==0: # 통로이면
                    v[ni][nj] = v[i][j] + 1 # 멀어진 한 칸 더해주기
                    q.append((ni, nj))
                elif arr[ni][nj]==3: #도착이면
                    v[ni][nj] = v[i][j] + 1
                    ans = v[ni][nj] - 2 # 출발과 도착칸 빼주기
                    flag = 1

    print(f'#{tc} {ans}')




