import sys
sys.stdin = open('input.txt', 'r')

def srt(lst): # sort함수 만들기
    n = len(lst)
    for i in range(n-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j + 1] = lst[j+1], lst[j]

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for lst in adj:
        srt(lst)

    v = [0]*(v+1) # 방문 표시
    q = [] # queue
    alst = []
    s = 1 # 시작 정점은 1
    q.append(s)
    alst.append(s)
    while q:
        t = q.pop(0)
        if v[t] == 0:
            v[t] = 1
        for e in adj[t]:
            if v[e] == 0 and e not in q: # 중복제거
                q.append(e)
                alst.append(e)

    print(f'#{tc}', *alst)
