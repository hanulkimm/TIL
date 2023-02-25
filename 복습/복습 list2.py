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

# 특별한 정렬 ##
t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(10):
        idx = i
        for j in range(i+1, n):
            if i % 2 == 0:
                if lst[idx] < lst[j]:
                    idx = j
            else:
                if lst[idx] > lst[j]:
                    idx = j
        lst[i], lst[idx] = lst[idx], lst[i]
    print(f'#{tc+1}', *lst)


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

## 149963 이진탐색 연습 ##

# 이진탐색 사용
def BinarySearch(lst, n, key):
    st = 0
    end = n-1
    while st <= end:
        middle = (st + end) // 2
        if lst[middle] == key:
            return middle +1
        elif lst[middle] < key:
            st = middle +1
        else:
            end = middle -1
    return 0


t = int(input())
for tc in range(t):
    n, key = map(int, input().split())
    lst = list(map(int, input().split()))
    print(BinarySearch(lst, n, key))

   # 다른 방법으로
    i = 0
    while i < n and lst[i] < key:
        i += 1
    if i < n and lst[i] == key:
        print(f'#{tc+1} {i+1}')
    else:
        print(f'#{tc+1} {0}')

## ladder ##

for tc in range(3):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    ci = 99
    for j in range(101):
        if arr[ci][j] == 2:
            cj = j
    while ci > 0:
        arr[ci][cj] = 0
        di = [0, 0, -1] # 좌 우 상
        dj = [-1, 1, 0]
        for k in range(3):
            ni, nj = ci + di[k], cj + dj[k]
            if arr[ni][nj]==1 and 0<=ni<100 and 0<=nj<100:
                ci, cj = ni, nj
                break
    # while ci > 0:
    #     arr[ci][cj] == 0:
    #     if arr[ci][cj-1] ==1:
    #         cj -= 1
    #     elif arr[ci][cj+1] == 1:
    #         cj += 1
    #     else:
    #         ci -= 1
                
    print(f'#{tc+1} {cj-1}')

## 이진탐색 게임 ##

def BinarySearch(st, end, key):
    cnt = 1
    while st <= end:
        middle = int((st + end) / 2)
        if middle == key:
            return cnt
        elif middle < key:
            st = middle
            cnt += 1
        else:
            end = middle
            cnt += 1


t = int(input())
for tc in range(t):
    p, a, b = map(int, input().split())
    if BinarySearch(1,p,a) < BinarySearch(1,p,b):
        ans = 'A'
    elif BinarySearch(1,p,a) > BinarySearch(1,p,b):
        ans = 'B'
    else:
        ans = 0

    print(f'#{tc+1} {ans}')

## 달팽이 ##
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    di = [0, 1, 0, -1]  # 우 하 좌 상
    dj = [1, 0, -1, 0]
    i = j = 0
    dr = 0
    for cnt in range(1, n ** 2 + 1):
        arr[i][j] = cnt
        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0 : #순서 조심!!!
            i, j = ni, nj
        else:
            dr = (dr + 1) % 4
            i, j = i + di[dr], j + dj[dr]
    for lst in arr:
        print(*lst)