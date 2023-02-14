import sys
sys.stdin = open('input.txt', 'r')

def dfs_stk(start):
    v = [0] * (V+1)
    stk = []

    s = start
    v[s] = 1
    alst.append(s)

    while True:
         for e in range(1, V+1):
             if v[e] == 0 and adj[s][e]:
                 stk.append(s)
                 s = e
                 v[s] = 1
                 alst.append(s)
                 break
         else:
            if stk:
                s = stk.pop()
            else:
                break


t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s][e] = adj[e][s] = 1
    alst = []
    dfs_stk(1)
    print(f'#{tc}', *alst)



