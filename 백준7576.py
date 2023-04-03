import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def exist(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                return True
    return False

def bfs(i,j):
    arr[i][j]=0
    q = deque()
    q.append((i,j))

    while q:
        si,sj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0:
                arr[ni][nj]=1
                q.append((ni,nj))

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while exist(arr):
    ans += 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                bfs(i,j)
print(ans)