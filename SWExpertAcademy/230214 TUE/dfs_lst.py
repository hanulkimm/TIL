import sys
sys.stdin = open('input.txt', 'r')

# DFS 풀이 2
# sort 이용


def dfs_stk(start):
    v = [0] * (V+1)
    stk = []

    s = start
    v[s] = 1
    alst.append(s)

    while True:
         for e in adj[s]:
             if v[e] == 0:
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
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    for i in range(1, V+1):
        adj[i].sort()

    alst = []
