import sys
sys.stdin = open('input.txt', 'r')

tc, n = map(int, input().split())
adj = [[0]*(n+1)]
for _ in range(n):
    s, e = map(int, input().split())
    adj[s].append(e)

s = 0
v = [[0]*(n+1)]
stk = []
v[0] = 1
ans = 0
while True:
    for e in adj[s]:
        stk.append(s)
        s = e
        v[s] = 1
        break
    else:
        if s == e:
            ans = 1
            break
        else:
            if stk:
                s = stk.pop()
            else:
                break
print(ans)