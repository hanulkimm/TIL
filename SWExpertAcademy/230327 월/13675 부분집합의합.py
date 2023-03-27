import sys
sys.stdin = open('input.txt', 'r')

def dfs(i,cnt,sm):
    global ans
    if i == N:
        if cnt==CNT and sm==K:
            ans += 1
        return
    else:
        dfs(i+1, cnt+1, sm+lst[i])
        dfs(i+1, cnt, sm)

t = int(input())
for tc in range(1, t+1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12
    ans = 0
    dfs(0,0,0)

    print(f'#{tc} {ans}')