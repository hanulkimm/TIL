import sys
sys.stdin = open('input.txt', 'r')

def pre(n):
    global cnt
    if n: # 0이 아닐 때
        cnt += 1
        pre(left[n])
        pre(right[n])

t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    left = [0] * (e+2)
    right = [0] * (e+2)
    for i in range(e):
        p, c = lst[i*2], lst[i*2+1]
        if left[p] ==0:
            left[p]=c
        else:
            right[p] = c
    cnt = 0
    pre(n)
    print(f'#{tc} {cnt}')

