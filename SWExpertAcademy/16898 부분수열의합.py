def dfs(i,sm):
    global ans
    if k < sm: # 가지치기
        return
    if i==n: # 끝까지 돌렸을 때
        if sm==k: # 합이 K이면
            ans += 1
            return
    else:
        dfs(i+1,sm+lst[i])
        dfs(i+1,sm)

t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')