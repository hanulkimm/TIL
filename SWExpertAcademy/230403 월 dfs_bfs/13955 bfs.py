def bfs(i):
    q = []
    q.append(i)
    v[i]=1
    alst.append(i)
    while q:
        s = q.pop(0)
        for j in adj[s]:
            if v[j]==0:
                v[j]=1
                q.append(j)
                alst.append(j)


t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    v = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    for lst in adj:
        lst.sort()
    alst = []
    bfs(1)
    print(f'#{tc}', *alst)