def dfs(i, lst):
    global ans
    if i==n:
        lst = lst + [1]
        tmp = 0
        for k in range(n):
            tmp += arr[lst[k]-1][lst[k+1]-1]
        if ans > tmp:
            ans = tmp
    else:
        for j in range(n):
            if v[j]==0:
                v[j]=1
                lst.append(p[j])
                dfs(i+1, lst)
                v[j]=0
                lst.pop()

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    p = [i for i in range(1, n+1)]
    v = [0] * n
    v[0]=1
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 1e9
    dfs(1, [1]) # idx, lst
    print(f'#{tc} {ans}')