import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    start, key = map(int, input().split())
    s = start
    v = [0] * (V + 1)
    stk = []
    v[s] = 1
    ans = 0
    while True:
        for e in adj[s]:
            if v[e] == 0:
                stk.append(s)
                s = e
                v[s] = 1
                break
        else:
            if s == key:
                ans = 1
                break
            else:
                if stk:
                    s = stk.pop()
                else:
                    ans = 0
                    break
    print(f'#{tc} {ans}')

