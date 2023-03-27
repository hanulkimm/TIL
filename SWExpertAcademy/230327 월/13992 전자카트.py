import sys
sys.stdin = open('input.txt', 'r')

def perm(i, k):
    if i == k:
        tmp = []
        for num in p:
            tmp.append(num)
        num_lst.append(tmp)
    else:
        for j in range(k):
            if used[j]==0:
                p[i]=N[j]
                used[j] = 1
                perm(i+1,k)
                used[j] = 0

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [0] * (n-1)
    N = [i for i in range(2, n+1)]
    used = [0] * (n-1)
    num_lst = []
    perm(0, n-1)
    ans = 1e9
    for lst in num_lst:
        lst = [1] + lst + [1]
        tmp_ans = 0
        for num in range(n):
            tmp_ans += arr[lst[num]-1][lst[num+1]-1]
        if ans > tmp_ans:
            ans = tmp_ans
    print(f'#{tc} {ans}')
