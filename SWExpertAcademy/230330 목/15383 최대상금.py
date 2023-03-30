import sys

sys.stdin = open('input.txt', 'r')

def dfs(cnt, lst):
    global ans
    if cnt == m:
        if lst[0] < ans//10**(n-1):
            return
        tmp = 0
        for k in range(n):
            tmp += 10 ** k * lst[n - 1 - k]
        if ans < tmp:
            ans = tmp
        return
    for i in range(n):
        for j in range(n):
            if j != i and lst[i]!=lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                dfs(cnt + 1, lst)
                lst[i], lst[j] = lst[j], lst[i]

t = int(input())
for tc in range(1, t + 1):
    lst, m = input().split()
    m = int(m)
    lst = list(map(int, lst))
    n = len(lst)
    ans = 0
    v = [0]*n
    dfs(0, lst)
    print(f'#{tc} {ans}')
