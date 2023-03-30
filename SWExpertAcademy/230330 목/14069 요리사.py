def dfs(depth, i):
    global ans
    if depth==n//2:
        tmp1, tmp2 = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if v[i] and v[j]:
                    tmp1 += arr[i][j] + arr[j][i]
                elif v[i]==0 and v[j]==0:
                    tmp2 += arr[i][j] + arr[j][i]
        ans = min(ans, abs(tmp1-tmp2))
        return

    for j in range(i, n):
        if v[j]==0:
            v[j]=1
            dfs(depth+1, j+1)
            v[j]=0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    v = [0] * n
    ans = 1e9
    dfs(0, 0) # 깊이, idx
    print(f'#{tc} {ans}')