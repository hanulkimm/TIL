import sys
sys.stdin = open('input.txt', 'r')

def pre(start):
    i = start
    print(i, end=' ')
    if left[i] > 0:
        pre(left[i])
    if right[i]>0:
        pre(right[i])


t = int(input())
for tc in range(1, t+1):
    V = int(input()) # 정점 개수
    E = V-1 # 간선 개수
    lst = list(map(int, input().split()))
    left = [0] * (V+1)
    right = [0] * (V+1)
    for i in range(E):
        p, c = lst[i*2], lst[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    print(f'#{tc}', end=' ')
    pre(1)