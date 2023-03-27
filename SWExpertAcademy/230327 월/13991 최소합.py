import sys
sys.stdin = open('input.txt', 'r')

def bfs(si,sj):
    global ans
    q = []
    v = [[0]*n for _ in range(n)]
    q.append((si,sj))
    v[si][sj] = arr[si][sj]
    while q:
        ci, cj = q.pop(0)
        for di,dj in ((0,1), (1,0)): # 오른쪽, 아래
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<n:
                if v[ni][nj]==0 or v[ni][nj] > v[ci][cj]+arr[ni][nj]:
                    v[ni][nj]=v[ci][cj]+arr[ni][nj]
                    q.append((ni,nj))
    ans = v[n - 1][n - 1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    bfs(0,0)
    print(f'#{tc} {ans}')