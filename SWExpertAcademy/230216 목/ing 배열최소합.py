import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm):
    global ans
    if ans <= sm:
        return
    if i == N:
        if ans > sm:
            ans = sm
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(i+1, sm + arr[i][j])
            v[j] = 0 # 반드시 다시 되돌려놓기


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 10 * N
    dfs(0, 0)
    print(f'#{tc} {ans}')



