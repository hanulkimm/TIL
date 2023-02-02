import sys
sys.stdin = open('input.txt','r')

def my_min():
    mn = 1001
    min_idx = -1
    for i in range(100):
        if mn > lst[i]:
            mn = lst[i]
            min_idx = i
    return min_idx

def my_max():
    mx = -1
    max_idx = -1
    for i in range(100):
        if mx < lst[i]:
            mx = lst[i]
            max_idx = i
    return max_idx


for tc in range(10):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        lst[my_min()] += 1
        lst[my_max()] -= 1

    print(f'#{tc+1} {lst[my_max()] - lst[my_min()]}')

