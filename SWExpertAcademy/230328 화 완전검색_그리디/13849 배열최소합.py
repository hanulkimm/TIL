import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm):
    global ans
    if ans<=sm:
        return
    if i == n:
        if ans > sm:
            ans = sm
    else:
        for j in range(n):
            if v[j]==0:
                v[j]=1
                dfs(i+1, sm+arr[i][j])
                v[j]=0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v =[0]*n
    ans = 100 * n
    dfs(0,0) # 시작점, 합
    print(f'#{tc} {ans}')