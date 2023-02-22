import sys
sys.stdin = open('input.txt', 'r')

def one(i, j):
    global cnt
    i, j = i, j

    while True:
        flag = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[i][j] + 1 == arr[ni][nj]:
                cnt += 1
                i, j = ni, nj
                flag = False
        if flag: # 더 이상 갈 수 없으면
            break


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mx = 0
    ans = 0
    for i in range(n):
        for j in range(n):
            s = arr[i][j]
            cnt = 1
            one(i, j)

            if mx < cnt: # 더 많은 방을 이동하는 경우
                mx = cnt
                ans = s
            if mx == cnt: # 이동 횟수 같다면 작은수 출력
                if ans > s:
                    ans = s

    print(f'#{tc} {ans} {mx}')
