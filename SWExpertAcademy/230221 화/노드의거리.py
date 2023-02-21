import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    s, g = map(int, input().split())

    v = [0] * (V+1) # 방문 표시
    q = []
    q.append(s)
    v[s] = 1

    ans = 0
    while q:
        if ans != 0:
            break
        t = q.pop(0)
        for e in adj[t]:
            if v[e]==0: # 미방문
                v[e] = v[t] + 1 # 거리 1씩 증가
                q.append(e)
                if e == g: # 도착하면
                    ans = v[e] -1 # 출발점 빼주기
                    break
    print(f'#{tc} {ans}')