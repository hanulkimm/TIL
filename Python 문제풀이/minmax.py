import sys
sys.stdin = open('minmax.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    mn = lst[0]
    mx = lst[0]
    for i in range(1, n):
        if mn > lst[i]:
            mn = lst[i]
        if mx < lst[i]:
            mx = lst[i]
    print(f'#{tc+1} {mx-mn}')