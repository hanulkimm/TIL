def dfs(i):
    v[i]=1
    alst.append(i)
    for j in adj[i]:
        if v[j]==0:
            dfs(j)

t = int(input())
for tc in range(1, t+1):
    V, E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    v = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    for lst in adj:
        lst.sort()
    alst = []
    dfs(1)
    print(f'#{tc}',*alst)