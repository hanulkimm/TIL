import sys
sys.stdin = open('input.txt', 'r')
for _ in range(3):
    tc, n = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    lst = list(map(int, input().split()))

    for i in range(n):
        a, b = lst[i*2], lst[i*2+1]
        adj[a].append(b)

    s = 0 # 시작점은 0
    v = [0]*100
    stk = []
    v[0] = 1
    ans = 0
    while True:
        if ans ==1:
            break
        for e in adj[s]:
            if e == 99: # 도착점
                ans = 1
                break # for문 밖으로 break
            elif v[e] == 0:
                stk.append(s)
                s = e
                v[s] = 1
                break

        else:
            if stk:
                s = stk.pop()
            else:
                break
    print(f'#{tc} {ans}')