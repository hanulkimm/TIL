def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j]=0
    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = si+di,sj+dj
            if 0<=ni<n and 0<=nj<n: # 범위내
                if v[ni][nj]==-1 or v[ni][nj]>v[si][sj]+arr[ni][nj]: # 미방문 또는 방문한 다른 경우보다 복구 시간이 적은 경우
                    v[ni][nj]=v[si][sj]+arr[ni][nj]
                    q.append((ni,nj))

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    v = [[-1] * n for _ in range(n)]
    bfs(0,0) # 시작좌표, sum
    ans = v[n - 1][n - 1]
    print(f'#{tc} {ans}')