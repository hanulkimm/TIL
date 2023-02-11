## 13674 색칠하기 ##

#만약 여러 색이 겹쳐진다면 
#color = 1 2 3 4 5
#tbl = [0, 1, 2, 4, 8, 16]
t = int(input())
for tc in range(t):
    arr = [[0] * 10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2, col = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += col

    ans = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans +=1
    print(f'#{tc+1} {ans}')

## 부분집합의 합 ##
## 공집합 제외 합이 0 이 되는 경우
t = int(input())
for tc in range(t):
    lst = list(map(int, input().split()))
    n = len(lst)
    ans = 0
    for bit in range(1,1<<n):
        sm = 0
        for j in range(n):
            if bit & (1<<j):
                sm += lst[j]
        if sm == 0:
            ans = 1
            break
    print(f'#{tc+1} {ans}')



# 개수와 합이 주어진 조건과 일치하는 지 
t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    lst = [n for n in range(1,13)]

    ans = 0
    for bit in range(1<<12):
        cnt = sm = 0
        for j in range(12):
            if bit & (1<<j):
                cnt += 1
                sm += lst[j]
        if cnt == n and sm == k:
                ans += 1
    print(f'#{tc+1} {ans}')

    
## 델타 검색 ##
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n)]
    print(arr)

    di = [-1, 1, 0, 0] # 상 하 좌 우
    dj = [0, 0, -1, 1]
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0<=ni<n and 0<=nj<n:
                    if arr[i][j] < arr[ni][nj]:
                        ans += arr[ni][nj] - arr[i][j]
                    else:
                        ans += arr[i][j] - arr[ni][nj]
    print(f'#{tc+1} {ans}')

## 13673 sum ##

for tc in range(2):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    mx = 0
    for i in range(100): # 행 별 합 구하기
        sm = 0
        for j in range(100):
            sm += arr[i][j]
        if mx < sm:
            mx = sm
    for j in range(100): # 열 별 합 구하기
        sm = 0
        for i in range(100):
            sm += arr[i][j]
        if mx < sm:
            mx = sm
    sm1 = 0
    sm2 = 0
    for i in range(100): # 대각선
        sm1 += arr[i][i]
        sm2 += arr[i][99-i]
    if mx < sm1:
        mx = sm1
    if mx < sm2:
        mx = sm2
    print(f'#{tc+1} {mx}')

'''ans = 0
sm3 = sm4 = 0
for i in range(100):
    sm1 = sm2 = 0
    for j in range(100):
        sm1 += arr[i][j]
        sm2 += arr[j][i]
    if ans < sm1:
        ans = sm1
    if ans < sm2:
        ans = sm2
    sm3 += arr[i][i]
    sm4 += arr[i]arr[99-i]
if ans < sm3: ans = sm3
if ans < sm4: ans = sm4'''

