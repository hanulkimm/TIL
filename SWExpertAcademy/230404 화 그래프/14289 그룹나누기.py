import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)]=find_set(x)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    rep = [i for i in range(n+1)]
    for i in range(m):
        s,e = lst[i*2], lst[i*2+1]
        union(s,e)

    cnt = [0] * (n+1)
    for i in range(1,n+1):
        cnt[find_set(rep[i])]=1

    ans = sum(cnt)
    print(f'#{tc} {ans}')