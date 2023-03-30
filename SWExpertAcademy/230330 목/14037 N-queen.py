def queen(i,j):
    for di, dj in ((-1,-1),(-1,0),(-1,1)): # 왼쪽 대각선, 상, 오른쪽 대각선
        for k in range(1, n+1):
            ni,nj = i+di*k, j+dj*k
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==1:
                return 0
    return 1

def dfs(i):
    global ans
    if i==n:
        ans += 1
    else:
        for j in range(n):
            if queen(i,j):
                v[i][j]=1
                dfs(i+1)
                v[i][j]=0
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    v = [[0] * n for _ in range(n)]
    ans = 0
    dfs(0) # idx
    print(f'#{tc} {ans}')