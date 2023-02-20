## 부분집합 ##
def dfs(i, sm):
    global ans
    if sm > k:
        return
    elif i == n:
        if sm ==k:
            ans += 1
        return
    dfs(i+1, sm+lst[i])
    dfs(i+1, sm)

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)

    print(f'#{tc} {ans}')

## 
def dfs(i, sm):
    global ans
    if ans < sm:
        return
    if i == n:
        if ans > sm:
            ans = sm
    for j in range(n):
        if v[j] == 0:
            v[j]=1
            dfs(i+1, sm+arr[i][j])
            v[j]=0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    dfs(0,0)